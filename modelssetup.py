# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Appointments(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    package = models.CharField(max_length=50)
    date_booked = models.CharField(max_length=50)
    time_booked = models.CharField(max_length=30)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CandidateJobApplications(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    job_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'candidate_job_applications'


class CandidateJobLikes(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    job_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'candidate_job_likes'


class CandidateOrders(models.Model):
    user_id = models.PositiveBigIntegerField()
    order_id = models.CharField(max_length=100)
    order_invoice = models.CharField(max_length=100)
    order_total = models.CharField(max_length=100)
    order_contact = models.CharField(max_length=100)
    status = models.IntegerField()
    candidates = models.TextField(db_collation='utf8mb4_bin')
    plan = models.TextField(db_collation='utf8mb4_bin')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'candidate_orders'


class CandidateSpecialisms(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    specialism_id = models.PositiveBigIntegerField()
    specialties = models.TextField(db_collation='utf8mb4_bin')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'candidate_specialisms'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.IntegerField()
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=355)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CompanySizes(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_sizes_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_sizes'


class CompanyTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_types_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_types'


class Contacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(db_collation='utf8mb4_bin')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class ContingencyHirings(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    job_title = models.TextField(blank=True, null=True)
    industry = models.TextField(blank=True, null=True)
    service = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contingency_hirings'


class ContractTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_types_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_types'


class DiscountCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.TextField()
    percent = models.FloatField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_codes'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EducationLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    experiences_id = models.PositiveBigIntegerField()
    education_levels_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'education_levels'


class EmployerProfiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    specialism_id = models.PositiveBigIntegerField()
    industry = models.ForeignKey('Industries', models.DO_NOTHING)
    company_type = models.ForeignKey(CompanyTypes, models.DO_NOTHING)
    company_size_id = models.PositiveBigIntegerField()
    company_name = models.CharField(max_length=200)
    tag_line = models.CharField(max_length=200)
    search_and_listing = models.IntegerField()
    facebook = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    linkedin = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    est_since = models.TextField()
    complete_address = models.TextField(blank=True, null=True)
    description = models.TextField()
    notification_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employer_profiles'


class Employers(models.Model):
    employers_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    website = models.TextField()
    social_media = models.TextField(db_collation='utf8mb4_bin')
    phone_number = models.CharField(max_length=200)
    country_code = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employers'


class ExperienceDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_current_job = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    job_title = models.DateField()
    company_name = models.DateField()
    job_location_city = models.CharField(max_length=200)
    job_location_state = models.CharField(max_length=200)
    job_location_county = models.CharField(max_length=200)
    country_code = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experience_details'


class Experiences(models.Model):
    id = models.BigAutoField(primary_key=True)
    experiences_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiences'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Industries(models.Model):
    id = models.BigAutoField(primary_key=True)
    industries_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industries'


class JobLevels(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_levels'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    specialism_id = models.PositiveBigIntegerField()
    industry_id = models.PositiveBigIntegerField()
    contract_type_id = models.PositiveBigIntegerField()
    education_level_id = models.PositiveBigIntegerField()
    experience_id = models.PositiveBigIntegerField()
    jobs_title = models.TextField()
    search_and_listing = models.IntegerField()
    experience_length = models.TextField()
    experience_level = models.TextField()
    qualifications_competencies = models.TextField()
    duties_responsibilities = models.TextField()
    offered_salary = models.TextField()
    address = models.TextField()
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.IntegerField()
    languages = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    jobs_description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    application_deadline = models.DateField()
    is_company_name_hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Languages(models.Model):
    language_names = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'languages'


class Leads(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads'


class LocationOfInterest(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_of_interest'


class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.PositiveBigIntegerField()
    uuid = models.CharField(max_length=36, blank=True, null=True)
    collection_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=255, blank=True, null=True)
    disk = models.CharField(max_length=255)
    conversions_disk = models.CharField(max_length=255, blank=True, null=True)
    size = models.PositiveBigIntegerField()
    manipulations = models.TextField(db_collation='utf8mb4_bin')
    custom_properties = models.TextField(db_collation='utf8mb4_bin')
    responsive_images = models.TextField(db_collation='utf8mb4_bin')
    order_column = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelHasPermissions(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_permissions'
        unique_together = (('permission', 'model_id', 'model_type'),)


class ModelHasRoles(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_roles'
        unique_together = (('role', 'model_id', 'model_type'),)


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    client_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.PositiveBigIntegerField()
    client_id = models.PositiveBigIntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    secret = models.CharField(max_length=100, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class Orders(models.Model):
    employer_id = models.IntegerField()
    number_of_candidates = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.IntegerField()
    payment_type = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'orders'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PostTag(models.Model):
    post = models.ForeignKey('Posts', models.DO_NOTHING)
    tag = models.ForeignKey('Tags', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'post_tag'


class Posts(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.BigIntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    sub_category_id = models.PositiveBigIntegerField()
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=355)
    excerpt = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published = models.IntegerField()
    metadata = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Profiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    specialism_id = models.TextField(db_collation='utf8mb4_bin')
    experiences_id = models.PositiveBigIntegerField()
    education_levels_id = models.PositiveBigIntegerField()
    job_title = models.TextField(blank=True, null=True)
    personal_statement = models.TextField(blank=True, null=True)
    personal = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    portfolio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    job_level = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    honors = models.TextField(blank=True, null=True)
    availability_status = models.IntegerField()
    metadata = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class RoleHasPermissions(models.Model):
    permission = models.OneToOneField(Permissions, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'
        unique_together = (('permission', 'role'),)


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Specialisms(models.Model):
    id = models.BigAutoField(primary_key=True)
    specialty = models.TextField()
    type = models.TextField()
    specific_specialty = models.TextField(db_collation='utf8mb4_bin')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialisms'


class Specialities(models.Model):
    id = models.BigAutoField(primary_key=True)
    specialities_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialities'


class SubCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    category_id = models.PositiveBigIntegerField()
    name = models.TextField()
    slug = models.TextField()
    description = models.TextField(blank=True, null=True)
    metadata = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_categories'


class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey(Accounts, models.DO_NOTHING)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    username = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(unique=True, max_length=50)
    phone = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    industry = models.IntegerField(blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    provider_id = models.CharField(max_length=255, blank=True, null=True)
    metadata = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    owner = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    bio = models.TextField()
    city = models.CharField(max_length=215)
    country = models.CharField(max_length=215)
    job_title = models.CharField(max_length=215)
    availability_status = models.CharField(max_length=215)
    password2 = models.CharField(max_length=215)
    profile_pic = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
