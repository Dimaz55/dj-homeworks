import pytest
from django.urls import reverse
from django.utils.http import urlencode

from students.models import Course
from students.serializers import CourseSerializer


@pytest.mark.django_db
def test_courses_detail(api_client, course_factory):
    courses = course_factory(_quantity=1)
    url = reverse('courses-detail', args=[courses[0].id])
    resp = api_client.get(url)
    assert resp.status_code == 200
    resp_json = resp.json()
    course = CourseSerializer(instance=courses[0])
    assert resp_json == course.data


@pytest.mark.django_db
def test_courses_list(api_client, course_factory):
    url = reverse("courses-list")
    courses = course_factory(_quantity=10)
    resp = api_client.get(url)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json) == 10
    courses = CourseSerializer(instance=courses, many=True)
    assert resp_json == courses.data


@pytest.mark.django_db
def test_courses_filter_by_id(api_client, course_factory):
    courses = course_factory(_quantity=5)
    url = reverse("courses-list")
    kwargs = {'id': courses[3].id}
    url += '?' + urlencode(kwargs)
    resp = api_client.get(url)
    assert resp.status_code == 200
    resp_json = resp.json()
    course = CourseSerializer(instance=courses[3])
    assert resp_json[0]['id'] == course.data['id']


@pytest.mark.django_db
def test_courses_filter_by_name(api_client, course_factory):
    courses = course_factory(_quantity=5)
    url = reverse("courses-list")
    kwargs = {'name': courses[4].name}
    url += '?' + urlencode(kwargs)
    resp = api_client.get(url)
    assert resp.status_code == 200
    resp_json = resp.json()
    course = CourseSerializer(instance=courses[4])
    assert resp_json[0]['name'] == course.data['name']


@pytest.mark.django_db
def test_courses_api_create(api_client):
    course_count_before = Course.objects.count()
    url = reverse("courses-list")
    data = {'name': 'Testcourse'}
    resp = api_client.post(url, data=data)
    assert resp.status_code == 201
    assert course_count_before + 1 == Course.objects.count()


@pytest.mark.django_db
def test_courses_api_update(api_client, course_factory):
    courses = course_factory(_quantity=1)
    url = reverse("courses-detail", args=[courses[0].id])
    data = {'name': 'Testcourse'}
    resp = api_client.patch(url, data=data)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json['name'] == 'Testcourse'


@pytest.mark.django_db
def test_courses_api_delete(api_client, course_factory):
    courses = course_factory(_quantity=1)
    courses_count = Course.objects.count()
    url = reverse("courses-detail", args=[courses[0].id])
    resp = api_client.delete(url)
    assert resp.status_code == 204
    assert courses_count - 1 == Course.objects.count()


@pytest.mark.django_db
def test_students_create(api_client, student_factory, settings):
    assert settings.MAX_STUDENTS_PER_COURSE == 21
