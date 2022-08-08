from django.db import models
from django.utils import timezone


class Client(models.Model):
    client_name = models.CharField(max_length=200)
    role = models.CharField(max_length=20)
    bd_manager = models.CharField(max_length=20)
    recruiter = models.CharField(max_length=20)
    crm_date = models.DateField(max_length=20)
    date_sent_requesting_candidate_salary = models.DateTimeField(default=timezone.now, blank=True)
    date_received_candidate_salary = models.DateTimeField(default=timezone.now, blank=True)
    date_sent_recruitment = models.DateField(max_length=20)
    assigned_to_recruiter = models.DateField(max_length=20)
    first_time_a_candidate_moves_to_every_new_stage = models.DateField(max_length=20)
    first_final_candidate_profile_sent_to_bd_manager = models.DateField(max_length=20)
    candidate_selected = models.DateField(max_length=20)
    date_of_candidate_selected = models.DateField(max_length=20)
    resumes_sent = models.BooleanField()
    number_of_profiles_sent = models.IntegerField()
    selected = models.BooleanField()
    number_of_selected_candidate = models.IntegerField()
    candidate_proposed_salary_range = models.IntegerField()
    final_confirmed_salary_range = models.IntegerField()
    type_of_payout = models.CharField(max_length=150)
    total_no_of_Recruitment_days_for_first_final_Selection = models.IntegerField()
    total_no_of_recruitment_days_for_client_selected_candidate = models.IntegerField()

    def __str__(self):
        return self.client_name