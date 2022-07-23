from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.db import connections
from django.views import View
from django.urls import reverse_lazy
from django.contrib.sessions.models import Session

from candidate.models import Candidate
from .models import NtrcaResult
from .forms import NtrcaForms, NtrcaMarkForms, NtrcaMarkFormset
from .filters import CandidateFilter

class NtrcaHomeView(View):
    def get(self, request):
        ntrca = NtrcaResult.objects.all()
        filters = CandidateFilter(request.GET, queryset=ntrca)
        ntrca = filters.qs
        context = {
            'ntrca_all': ntrca,
            'filter': filters
        }
        return render(request, 'view_result.html', context)
    
    def post(self, request):
        pass

class NtrcaDateBoard(View):
    def get(self, request):
        form = NtrcaForms(request.POST)
        context = {'form': form}
        return render(request, 'enter_roll.html', context)
    
    def post(self, request):
        form = NtrcaForms(request.POST)
        date_of_interview = request.POST.get('interview_date' or None)
        board = request.POST.get('board' or None)
        try:
            candidate = Candidate.objects.filter(interview_date=date_of_interview, board=board)
        except Exception as e:
            print(f'candidate: {e}')
            candidate = None
        try:
            ntrca_result = NtrcaResult.objects.filter(interview_date=date_of_interview, board=board)
        except Exception as e:
            print(f'ntrca_result: {e}')
            ntrca_result = None
        request.session['date_of_interview']=date_of_interview
        request.session['board']=board
        if candidate:
            if form.is_valid():
                interview_date = form.cleaned_data['interview_date']
                board = form.cleaned_data['board']
                for can in candidate:
                    ntrca_result = NtrcaResult.objects.update_or_create(
                        interview_date=can.interview_date,
                        board=can.board,
                        roll=can.roll,
                        name=can.name,
                        father=can.father,
                        mother=can.mother,
                        subject_code=can.subject_code,
                        invoice=can.invoice
                    )
                return redirect('ntrca_result_create')
            else:
                context = {
                    'form': form,
                    'error': 'You are already registered!'
                    }
                return render(request, 'enter_roll.html', context)
        else:
            context = {
                'form': form,
                'error': 'Invalid!'
                }
            return render(request, 'enter_roll.html', context)


class NtrcaCreateResult(View):
    def get(self, request):
        date_of_interview = request.session.get('date_of_interview')
        board = request.session.get('board')
        candidate = NtrcaResult.objects.filter(interview_date=date_of_interview, board=board)
        formset = NtrcaMarkFormset(queryset=candidate)
        context = {
            'candidates': candidate,
            'formset': formset,
        }
        return render(request, 'enter_mark_copy.html', context)

    def post(self, request):
        date_of_interview = request.session.get('date_of_interview')
        board = request.session.get('board')
        candidate = NtrcaResult.objects.filter(interview_date=date_of_interview, board=board)
        formset = NtrcaMarkFormset(request.POST, queryset=candidate)
        for form in formset:
            if form.is_valid():
                s_number = form.cleaned_data['s_number']
                v_number = form.cleaned_data['v_number']
                comment = form.cleaned_data['comment']
                total_number = float(s_number) + float(v_number)
                candidate = form.save(commit=False)
                candidate.s_number = s_number
                candidate.v_number = v_number
                candidate.comment = comment
                candidate.total_number = total_number
                candidate.save()
        return redirect('ntrca_search_date')
        

class UpdateCandidate(View):
    def get(self, request, pk):
        candidate = NtrcaResult.objects.get(pk=pk)
        print(candidate)
        form = NtrcaMarkForms(instance=candidate)
        context = {
            'ntrca_result': candidate,
            'formset': form
        }
        return render(request, 'update_mark.html', context)
    def post(self, request, pk):
        candidate = NtrcaResult.objects.get(pk=pk)
        form = NtrcaMarkForms(request.POST, instance=candidate)
        if form.is_valid():
            s_number = form.cleaned_data['s_number']
            v_number = form.cleaned_data['v_number']
            comment = form.cleaned_data['comment']
            total_number = float(s_number) + float(v_number)
            candidate.s_number = s_number
            candidate.v_number = v_number
            candidate.comment = comment
            candidate.total_number = total_number
            candidate.save()
            return redirect(self.request.path_info)
        context = {
            'ntrca_result': candidate,
            'formset': form
        }
        return render(request, 'update_mark.html', context)
