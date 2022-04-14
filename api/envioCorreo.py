def __init__(data):
    import smtplib
    from email.message import EmailMessage  
    EMAIL_ADDRESS = 'bellastarhotel117@gmail.com'
    EMAIL_PASSWORD = 'Sistemas106'
    data=data
#contacts = ['YourAddress@gmail.com', 'test@example.com']
    
    msg = EmailMessage()
    msg['Subject'] = 'Correo de confirmacion de Reservacion'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = data.email

    msg.set_content('This is a plain text email')

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <div id=":282" class="ii gt" jslog="20277; u014N:xr6bB; 4:W251bGwsbnVsbCxbXV0."><div id=":283" class="a3s aiL "><p>Apreciado(a) {nombre} {apellido} .</p>
    <p>Esta es la confirmación de la cita para Carnival.</p>
    <p>Te estaremos esperando en Cerrada Zona Costera lote 21, manzana 91, 77727 Q.R.  Playa del Carmen, Quintana Roo el junio 6, 2021 a las 8:00 pm.</p>
    <p>Gracias por confiar en nosotros.</p>
    <p><span class="il">BellaStar</span><br>
    +994306007<br>
    <a href="https://josemanuel286.github.io/Proyecto-Hotel-Bellastar/index.html" target="_blank" data-saferedirecturl="https://josemanuel286.github.io/Proyecto-Hotel-Bellastar/index.html">Hotel Bellastar</a></p><div class="yj6qo"></div><div class="adL">

    </div></div></div>
        </body>
    </html>
    """.format(nombre=data.nombre, apellido=data.apellido), subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)