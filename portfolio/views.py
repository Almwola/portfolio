from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import ContactForm
from .models import Certification, Project, SkillCategory

SITE = {
    "name": "Mohamed Abd Elmwoli",
    "title": "Backend Developer",
    "email": "elmwola.404@gmail.com",
    "phone": "01110324549",
    "phone_intl": "+201110324549",
    "whatsapp": "https://wa.me/201110324549",
    "github": "https://github.com/Almwola",
    "linkedin": "https://www.linkedin.com/in/mohamed-abd-elmwola-aa77b9295/",
}

CV_PATH = settings.BASE_DIR / "portfolio" / "static" / "portfolio" / "assets" / "Mohamed-Abd-Elmwoli-CV.pdf"


def home(request):
    context = {
        "site": SITE,
        "skill_categories": SkillCategory.objects.prefetch_related("skills"),
        "projects": Project.objects.all(),
        "certifications": Certification.objects.all(),
    }
    return render(request, "portfolio/index.html", context)


@require_POST
def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        msg = form.save()
        if settings.CONTACT_NOTIFY_EMAIL and getattr(settings, "EMAIL_HOST", ""):
            send_mail(
                subject=f"[Portfolio] {msg.subject}",
                message=f"From: {msg.name} <{msg.email}>\n\n{msg.message}",
                from_email=None,
                recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
                fail_silently=True,
            )
        messages.success(request, "Message received. Thank you, I will get back to you.")
    else:
        messages.error(request, "Please fill in every field with a valid email address.")
    return redirect("/#contact")


def download_cv(request):
    if CV_PATH.exists():
        return FileResponse(open(CV_PATH, "rb"), as_attachment=True, filename="Mohamed-Abd-Elmwoli-CV.pdf")
    return HttpResponse(
        "The CV file has not been added yet. Place Mohamed-Abd-Elmwoli-CV.pdf in portfolio/static/portfolio/assets/.",
        status=404,
        content_type="text/plain",
    )
