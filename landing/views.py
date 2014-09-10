#encoding: utf-8
#System
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string

import StringIO
import qrcode
import xhtml2pdf.pisa as pisa


#Public APP views
def index(request):

    return render_to_response('landing/index.html',
                               {},
                               context_instance=RequestContext(request))


def confirm(request, idattendee):
    return render_to_response('landing/confirmar.html',
                               {},
                               context_instance=RequestContext(request))


def invitation(request, idattendee):
    response = HttpResponse(mimetype='application/pdf; charset=utf-8')

    #response['Content-Disposition'] = 'attachment; filename=test.pdf'

    qrCode = qrcode.QRCode(
                       version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4,
                       )

    qrCode.add_data('Some data')

    qrCode.make(fit=True)

    qrImage = qrCode.make_image()

    qrFile = StringIO.StringIO()

    qrImage.save(qrFile, "PNG")

    '''
    file_name = "static/test.png"
    image_file = open(file_name, 'w+')
    qrImage.save(image_file, "PNG")
    image_file.close()
    '''

    #import ipdb; ipdb.set_trace()
    imagen = qrImage.getdata()

    #import ipdb; ipdb.set_trace()

    #imagen = "data:image/png;base64, %s" % b64encode(qrFile.getvalue())
    imagen = "data:image/png;base64, %s" % qrFile.getvalue().encode("base64")

    pdfStringData = render_to_string('landing/pdf.html',
                                     {
                                        'QR_CODE'           : imagen,
                                        'PROTOCOL'          : 'http://',
                                        'HOSTNAME'          : request.get_host(),
                                        'CLIENT_TYPE'       : 'Agencia',
                                        'EVENT_TYPE_NAME'   : 'Título del evento',
                                        'CLIENT_NAME'       : 'Nombre',
                                        'CLIENT_SURNAME'    : 'Apellidos',
                                        'CLIENT_EMAIL'      : 'email@test.es',
                                        'CLIENT_WEB'        : 'www.test.es',
                                        'EVENT_PLACE'       : 'Edificio 1',
                                        'EVENT_ADDRESS'     : 'C/ No hay calle y menos número',
                                        'EVENT_CITY '       : 'Madrid',
                                        'EVENT_DATES'       : 'Días 2 de junio a las 09:00h'
                                    },
                                    context_instance=RequestContext(request))

    pdfStringData = pdfStringData.encode("UTF-8")

    pisa.showLogging()

    packet = StringIO.StringIO()

    pisa.CreatePDF(
        pdfStringData,
        dest=packet)

    packet.seek(0)

    response.write(packet.getvalue())
    return response
