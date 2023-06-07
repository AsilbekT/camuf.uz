# Generated by Django 4.1.1 on 2023-06-07 21:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Article Category',
                'verbose_name_plural': 'Article Categories',
            },
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'University email',
                'verbose_name_plural': 'University emails',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/db/gallery/')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='GraduateCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/db/news/')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('course_type', models.CharField(blank=True, max_length=200, null=True)),
                ('body', tinymce.models.HTMLField(blank=True, null=True)),
                ('duration', models.IntegerField()),
                ('catagory', models.CharField(default='graduate', max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Graduate Course',
                'verbose_name_plural': 'Graduate Courses',
            },
        ),
        migrations.CreateModel(
            name='InterestedPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Interested People',
                'verbose_name_plural': 'Interested People',
            },
        ),
        migrations.CreateModel(
            name='Leaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname_uz', models.CharField(default='', max_length=200)),
                ('fullname_en', models.CharField(default='', max_length=200)),
                ('fullname_ru', models.CharField(default='', max_length=200)),
                ('position_uz', models.CharField(default='', max_length=200)),
                ('position_en', models.CharField(default='', max_length=200)),
                ('position_ru', models.CharField(default='', max_length=200)),
                ('number', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telegram', models.CharField(default='', max_length=200)),
                ('instagram', models.CharField(default='', max_length=200)),
                ('facebook', models.CharField(default='', max_length=200)),
                ('about_uz', tinymce.models.HTMLField(blank=True, null=True)),
                ('about_en', tinymce.models.HTMLField(blank=True, null=True)),
                ('about_ru', tinymce.models.HTMLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='static/db/workers/')),
                ('catagory', models.CharField(default='leaders', max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Leader',
                'verbose_name_plural': 'Leaders',
            },
        ),
        migrations.CreateModel(
            name='NewsCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'News Category',
                'verbose_name_plural': 'New Categories',
            },
        ),
        migrations.CreateModel(
            name='UndergraduateCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/db/news/')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('course_type', models.CharField(blank=True, max_length=200, null=True)),
                ('body', tinymce.models.HTMLField(blank=True, null=True)),
                ('duration', models.IntegerField()),
                ('catagory', models.CharField(default='undergraduate', max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Undergraduate Course',
                'verbose_name_plural': 'Undergraduate Courses',
            },
        ),
        migrations.CreateModel(
            name='UniPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'University Number',
                'verbose_name_plural': 'University Numbers',
            },
        ),
        migrations.CreateModel(
            name='UniversityGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/db/unipics/')),
            ],
            options={
                'verbose_name': 'University picture',
                'verbose_name_plural': 'University Pictures',
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname_uz', models.CharField(default='', max_length=200)),
                ('fullname_en', models.CharField(default='', max_length=200)),
                ('fullname_ru', models.CharField(default='', max_length=200)),
                ('position_uz', models.CharField(default='', max_length=200)),
                ('position_en', models.CharField(default='', max_length=200)),
                ('position_ru', models.CharField(default='', max_length=200)),
                ('number', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telegram', models.CharField(default='', max_length=200)),
                ('instagram', models.CharField(default='', max_length=200)),
                ('facebook', models.CharField(default='', max_length=200)),
                ('about_uz', tinymce.models.HTMLField(blank=True, null=True)),
                ('about_en', tinymce.models.HTMLField(blank=True, null=True)),
                ('about_ru', tinymce.models.HTMLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='static/db/workers/')),
                ('catagory', models.CharField(default='leaders', max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent_of_graduations', models.IntegerField()),
                ('number_of_professors', models.IntegerField()),
                ('number_of_housing', models.IntegerField()),
                ('number_of_students', models.IntegerField()),
                ('about_university_title', tinymce.models.HTMLField()),
                ('about_university_body', tinymce.models.HTMLField()),
                ('about_university_image', models.ImageField(upload_to='static/db/about_university/')),
                ('university_location', models.CharField(blank=True, max_length=300, null=True)),
                ('phone_number', models.ManyToManyField(to='app.uniphone')),
                ('rector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.leaders')),
                ('university_email', models.ManyToManyField(to='app.emailaddress')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statues',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('body', tinymce.models.HTMLField()),
                ('date_created', models.DateField()),
                ('image', models.ImageField(upload_to='static/db/news/')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('news_catagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_catagory', to='app.newscatagory')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('body', tinymce.models.HTMLField()),
                ('date_created', models.DateTimeField()),
                ('image', models.ImageField(upload_to='static/db/news/')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('in_charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.workers')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('body', tinymce.models.HTMLField()),
                ('date_created', models.DateField()),
                ('image', models.ImageField(upload_to='static/db/article/')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('article_catagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_catagory', to='app.articlecatagory')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='AppliedStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('', "O'qish tilini tanlang"), ('en', 'Ingliz'), ('uz', "O'zbek"), ('ru', 'Rus')], max_length=200, null=True)),
                ('surname', models.CharField(max_length=200)),
                ('bot_id', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
                ('fathers_name', models.CharField(max_length=200)),
                ('passport_number', models.CharField(max_length=200)),
                ('passport_pdf', models.FileField(upload_to='static/users/passports')),
                ('country', models.CharField(choices=[('', 'Davlatizni tanlang'), ('AF', 'Afghanistan'), ('AX', 'Aland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia, Plurinational State of'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo, The Democratic Republic of the'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', "Côte d'Ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See (Vatican City State)'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran, Islamic Republic of'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia, Republic of'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia, Federated States of'), ('MD', 'Moldova, Republic of'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestinian Territory, Occupied'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('BL', 'Saint Barthélemy'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia and the South Sandwich Islands'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SS', 'South Sudan'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan, Province of China'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela, Bolivarian Republic of'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('WF', 'Wallis and Futuna'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('schooling', models.CharField(choices=[('', 'Tamomlagan bilim yurtini tastiqlovchi xujjat'), ("O'rta maktab", "O'rta maktab"), ('Litsey', 'Litsey'), ('Bilim yurti', 'Bilim yurti'), ('Boshqa', 'Boshqa')], max_length=200)),
                ('diploma', models.FileField(upload_to='static/users/diplomas')),
                ('social_status', models.CharField(choices=[('', 'Ijtimoiy xolat'), ('Yoshlar daftari', 'Yoshlar daftari'), ('Ayollar daftari', 'Ayollar daftari'), ('Temir daftar', 'Temir daftar'), ("Yo'q", "Yo'q"), ('Boshqa', 'Boshqa')], max_length=200)),
                ('social_status_file', models.FileField(upload_to='static/users/social_statuses')),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('accepted', models.BooleanField(default=False)),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program', to='app.undergraduatecourse')),
            ],
            options={
                'verbose_name': 'Applied Student',
                'verbose_name_plural': 'Applied Students',
            },
        ),
    ]
