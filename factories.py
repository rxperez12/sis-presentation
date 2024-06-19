# Examples of Factory Classes

from factory import LazyAttribute as Lazy, fuzzy
from core.fake import FAKE_LOCATIONS


# BASE FACTORY:
class UserFactory(factory.django.DjangoModelFactory):
    """Factory class that helps create test users."""

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    # is_student = False
    # is_staff = False
    # is_superuser = False
    # is_active = True
    date_joined = make_aware(datetime(2020, 1, 1))
    first_name = 'Jane'
    last_name = 'Smith'
    username = Lazy(lambda s: slugify(s.first_name + "-" + s.last_name))
    password = factory.PostGenerationMethodCall(
        '_factory_set_password', 'password')
    pronunciation = "name-pronunciation"
    nickname = "nickname"
    formal_name = "formal-name"
    pronoun = "they"
    email = factory.LazyAttribute(lambda s: f'{s.username}@us.com')
    email_public = True
    phone = '+1 415 555 1212'
    phone_public = False
    bio = "bio"
    location = "City, State"
    location_public = True
    github_username = "github-username"
    github_username_public = True
    twitter_username = "twitter_username"
    twitter_username_public = True
    linkedin_url = "https://www.linkedin.com/user"
    linkedin_url_public = True
    slack_userid = "U1234567890"
    personal_site_url = "https://personal-site.url/"
    personal_site_url_public = True
    # resume_file = factory.django.FileField(filename="resume.pdf")
    resume_link = "https://resume.url/"
    resume_public = False
    emergency_contact_name = "emergency-contact-name"
    emergency_contact_phone = '+1 415 555 1212'
    emergency_contact_relationship = "emergency-contact-relationship"
    tshirt_size = Lazy(lambda s: "w-l" if s.pronoun == "she" else "m-l")
    # signature = FileField for svg signature
    # photo = ImageField for photo
    mailing_address = "123 Fake Street"
    notes = "staff-only-notes"
    birthdate = make_aware(datetime(2000, 1, 1))
    country_of_origin = Country(code='CA')
    country_current = Country(code='US')
    # ethnicities = ManyToMany
    gender_identity = "unstated"
    prev_salary = 100000
    prev_titles = ""
    legally_authorized = True
    legally_authorized_notes = ""


# SUBCLASSED FROM USER FACTORY:
class _FakeUser(UserFactory):
    """Create realistic-fake user."""

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = Lazy(lambda s: slugify(f"{s.first_name} {s.last_name}"))
    pronunciation = Lazy(lambda s: "RAN-dum" if random() < 0.2 else "")
    nickname = Lazy(lambda s: "Ace" if random() < 0.2 else "")
    formal_name = Lazy(
        lambda s: f"Dr. {s.first_name} {s.last_name}" if random() < 0.2 else "")
    bio = factory.Faker("paragraph", nb_sentences=8)
    location = fuzzy.FuzzyChoice(FAKE_LOCATIONS)
    notes = Lazy(lambda s: "Fake note." if random() < 0.2 else "")


# SUBFACTORY EXAMPLE:
# subfactories are use when an attribute is a complex field ex. a foreign key to
# another model.
class CommunicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Communication
        django_get_or_create = ('id',)

    id = 1001
    user = factory.SubFactory(UserFactory)
    type = "email"
    sender = "Sender <sender@sender.com>"
    recipient = "Jane <jane@jane.com>"
    title = "Welcome"
    message = "message-body"
