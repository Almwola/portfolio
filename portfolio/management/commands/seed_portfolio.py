"""Load the portfolio content (only facts provided by Mohamed). Safe to re-run."""
from django.core.management.base import BaseCommand

from portfolio.models import Certification, Project, Skill, SkillCategory

GITHUB = "https://github.com/Almwola"  # profile link; replace per project in /admin

SKILLS = [
    ("Programming Languages", ["Python", "C++", "Java"]),
    ("Backend", ["Django", "Django REST Framework"]),
    ("Frontend", ["HTML", "CSS"]),
    ("Tools", ["Git", "GitHub", "Docker", "Postman"]),
    ("Computer Science", ["Object-Oriented Programming", "Data Structures", "Algorithms"]),
]

PROJECTS = [
    dict(
        slug="el-gehad-management-system",
        title="El-Gehad Management System",
        kind="Business / Inventory Management System",
        description="A management system designed for a business specializing in modern irrigation supplies.",
        features="Dashboard\nSales Management\nOrders Management\nInventory Management\nLow Stock Alerts\nPOS\nInvoices\nProfit Calculation\nReports\nAdmin / Cashier Roles\nLogin & Authentication",
        technologies="Python, Django, PostgreSQL, HTML, CSS",
        categories="backend django management",
        is_featured=True,
        note="Portfolio / training project. Currently prepared for deployment to a server.",
    ),
    dict(
        slug="e-commerce-backend-api",
        title="E-Commerce Backend API",
        kind="Backend / REST API",
        description="A backend API for an e-commerce application focusing on RESTful API development and backend functionality.",
        features="Product APIs\nAuthentication\nJWT Authentication\nOrders\nSerializers\nREST API Endpoints\nPassword Reset\nAPI Testing with Postman",
        technologies="Python, Django, Django REST Framework, Postman, Database",
        categories="backend django rest",
        is_featured=True,
    ),
    dict(
        slug="siwa-safari-backend",
        title="Siwa Safari Backend",
        kind="Travel / Tourism Backend API",
        description="A backend API for a tourism/travel application that manages landmarks, trips, bookings, users, and travel-related data. The frontend was developed separately.",
        features="User Registration\nLogin\nJWT Authentication\nAccess / Refresh Tokens\nTourist Landmarks\nTravel Types\nTrips\nBookings\nUser Profile\nUser Bookings\nREST APIs",
        technologies="Python, Django, Django REST Framework, SimpleJWT, Postman",
        categories="backend django rest",
        is_featured=True,
    ),
    dict(
        slug="nahda-schools-digital-communication-platform",
        title="Nahda Schools Digital Communication Platform",
        kind="School Management / Communication Platform",
        description="A Django web platform for school communication and management.",
        features="",
        technologies="Python, Django, HTML, CSS, Database",
        categories="django management",
    ),
    dict(
        slug="library-book-rental-system",
        title="Library / Book Rental System",
        kind="Library Management System",
        description="A library system built around authors, books, and borrowing.",
        features="Author Management\nBook Management\nBook Borrowing\nLibrary Records",
        technologies="Python, Django, Database",
        categories="django management",
    ),
    dict(
        slug="school-management-system",
        title="School Management System",
        kind="School Management System",
        description="A system for organizing students, classes, subjects, and results.",
        features="Classes\nStudents\nSubjects\nSubject Combinations\nNotices\nResults\nStudent/Class Organization",
        technologies="Python, Django, Database",
        categories="django management",
    ),
    dict(
        slug="el-nahda-clinics",
        title="El Nahda Clinics",
        kind="Clinic Management System",
        description="A clinic management system with accounts, login, and user profiles.",
        features="Clinic Management\nAccounts\nLogin\nUser Profiles\nClinic-related Data Management",
        technologies="Python, Django, Database, HTML, CSS",
        categories="django management",
    ),
]

CERTS = [
    dict(
        title="Django (REST API)",
        platform="M3aarf",
        kind="Course Completion / Achievement Certificate",
        issued_on="25 November 2025",
        number="d91ba6eb",
    ),
    dict(
        title="Python Programming Basics",
        platform="Mahara-Tech / ITI",
        kind="Course Completion",
    ),
]


class Command(BaseCommand):
    help = "Seed the portfolio with Mohamed's real content."

    def handle(self, *args, **options):
        for i, (cat, names) in enumerate(SKILLS):
            category, _ = SkillCategory.objects.update_or_create(name=cat, defaults={"order": i})
            for j, name in enumerate(names):
                Skill.objects.update_or_create(category=category, name=name, defaults={"order": j})

        for i, data in enumerate(PROJECTS):
            slug = data.pop("slug")
            data.setdefault("github_url", GITHUB)
            data["order"] = i
            Project.objects.update_or_create(slug=slug, defaults=data)

        for i, data in enumerate(CERTS):
            title = data.pop("title")
            data["order"] = i
            Certification.objects.update_or_create(title=title, defaults=data)

        self.stdout.write(self.style.SUCCESS("Portfolio content seeded."))
