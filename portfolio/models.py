from django.db import models


class SkillCategory(models.Model):
    name = models.CharField(max_length=80)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name_plural = "skill categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=80)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    kind = models.CharField("type", max_length=120, help_text="e.g. Backend / REST API")
    description = models.TextField()
    features = models.TextField(blank=True, help_text="One feature per line.")
    technologies = models.CharField(max_length=250, help_text="Comma separated.")
    categories = models.CharField(
        max_length=120,
        help_text="Space separated filter tags. Allowed: backend django rest management",
    )
    is_featured = models.BooleanField(default=False)
    note = models.CharField(max_length=250, blank=True, help_text="Short status note (optional).")
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True, help_text="Leave empty if there is no live demo.")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title

    @property
    def feature_list(self):
        return [line.strip() for line in self.features.splitlines() if line.strip()]

    @property
    def tech_list(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]


class Certification(models.Model):
    title = models.CharField(max_length=150)
    platform = models.CharField(max_length=150)
    kind = models.CharField("type", max_length=150)
    issued_on = models.CharField(max_length=60, blank=True, help_text="Free text, e.g. 25 November 2025")
    number = models.CharField("certificate number", max_length=60, blank=True)
    image = models.ImageField(upload_to="certificates/", blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} — {self.name}"
