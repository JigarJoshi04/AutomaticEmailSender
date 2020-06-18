from django.core.mail import send_mail

send_mail(
    'Subject Here',
    'Here is the message.',
    'jigar.pj@somaiya.edu',
    ['mahadevstationerynashik@gmail.com'],
    fail_silently=False,
)