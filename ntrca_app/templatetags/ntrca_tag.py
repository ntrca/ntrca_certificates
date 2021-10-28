import qrcode
from django import template


register = template.Library()


@register.filter(name='qrcode')
def qrcode(obj):
    img = qrcode.make('Some data here')
    type(img)  # qrcode.image.pil.PilImage
    img.save("some_file.png")
    print(img, 'image')
    return img
        