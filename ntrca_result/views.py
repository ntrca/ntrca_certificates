from django.shortcuts import render, redirect
from django.views.generic import View
from ntrca_app.utilities import ExamsName

from candidate.models import Candidate
from ntrca_app.models import NTRCACirtificate
from .models import NtrcaResult
from .forms import NtrcaForms, NtrcaMarkForms, NtrcaMarkFormset
from .filters import CandidateFilter

class ResultHomeView(View):
    def get(self, request, exam_pk):
        exam_name = ExamsName.objects.get(pk=exam_pk)
        ntrca = NtrcaResult.objects.filter(
            exam_name=exam_name
        )
        filters = CandidateFilter(request.GET, queryset=ntrca)
        ntrca = filters.qs
        context = {
            'ntrca_all': ntrca,
            'filter': filters,
            'object': exam_name
        }
        return render(request, 'view_result.html', context)


class DateBoardView(View):
    def get(self, request, pk):
        exam_name = ExamsName.objects.get(pk=pk)
        form = NtrcaForms(request.POST)
        context = {
            'form': form,
            'object': exam_name
        }
        return render(request, 'enter_roll.html', context)
    
    def post(self, request, pk):
        exam_name = ExamsName.objects.get(pk=pk)
        form = NtrcaForms(request.POST)
        date_of_interview = request.POST.get('interview_date' or None)
        board = request.POST.get('board' or None)
        candidate = Candidate.objects.filter(
            interview_date=date_of_interview, board=board,
            exam_name=exam_name
        )
        request.session['date_of_interview']=date_of_interview
        request.session['board']=board
        if candidate:
            if form.is_valid():
                board = form.cleaned_data['board']
                for can in candidate:
                    board = float(can.board)
                    try:
                        data = NtrcaResult.objects.get(roll=can.roll)
                        print(f"Data Found {data.roll}")
                    except Exception as e:
                        data = NtrcaResult.objects.create(
                            exam_name=exam_name,
                            roll=can.roll,
                        )
                return redirect('markes_entry', pk=exam_name.pk)
            else:
                context = {
                    'form': form,
                    'error': 'You are already registered!',
                    'object': exam_name
                    }
                return render(request, 'enter_roll.html', context)
        else:
            context = {
                'form': form,
                'error': 'Invalid!',
                'object': exam_name
                }
            return render(request, 'enter_roll.html', context)


class MarkesEntry(View):
    def get(self, request, pk):
        exam_name = ExamsName.objects.get(pk=pk)
        date_of_interview = request.session.get('date_of_interview')
        board = request.session.get('board')
        candidate = NtrcaResult.objects.filter(
            interview_date=date_of_interview, board=float(board),
            exam_name=exam_name
        )
        formset = NtrcaMarkFormset(queryset=candidate)
        context = {
            'candidates': candidate,
            'formset': formset,
            'object': exam_name
        }
        return render(request, 'enter_mark_copy.html', context)

    def post(self, request, pk):
        exam_name = ExamsName.objects.get(pk=pk)
        date_of_interview = request.session.get('date_of_interview')
        board = request.session.get('board')
        candidate = NtrcaResult.objects.filter(
            interview_date=date_of_interview, board=float(board),
            exam_name=exam_name
        )
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
                if exam_name.viva_pass == float(v_number):
                    try:
                        NTRCACirtificate.objects.get(
                            roll=candidate.roll
                        )
                    except Exception as e:
                        NTRCACirtificate.objects.create(
                            exam_name=exam_name,
                            roll=candidate.roll,
                            subject_code=candidate.subject_code,
                            name=candidate.name,
                            ssc_result=candidate.s_result,
                            hsc_result=candidate.h_result,
                            invoice=candidate.invoice,
                            dob=candidate.dob,
                            viva_mark=total_number
                        )
        return redirect('ntrca_search_date', pk=exam_name.pk)


class UpdateCandidate(View):
    def get(self, request, pk, exam_pk):
        exam_name = ExamsName.objects.get(pk=exam_pk)
        candidate = NtrcaResult.objects.get(pk=pk, exam_name=exam_name)
        form = NtrcaMarkForms(instance=candidate)
        context = {
            'ntrca_result': candidate,
            'formset': form,
            'object': exam_name
        }
        return render(request, 'update_mark.html', context)
    def post(self, request, pk, exam_pk):
        exam_name = ExamsName.objects.get(pk=exam_pk)
        candidate = NtrcaResult.objects.get(pk=pk, exam_name=exam_name)
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
            return redirect('result_home', exam_pk=exam_name.pk)
        context = {
            'ntrca_result': candidate,
            'formset': form,
            'object': exam_name
        }
        return render(request, 'update_mark.html', context)
