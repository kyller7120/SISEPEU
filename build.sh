set -o errexit

python -m pip install -r ./requirements.txt

python manage.py collectstatic --no-input
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('grupo28', 'grupo28', 'covik19')" | python manage.py shell
python manage.py migrate
