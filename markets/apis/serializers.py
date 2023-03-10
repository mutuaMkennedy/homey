from rest_framework import serializers
from django.contrib.auth import get_user_model
from markets import models
from django.db.models import Avg

# referencing the custom user model
User = get_user_model()

class JobPostProposalSerializer(serializers.ModelSerializer):
    proposal_sender_object = serializers.SerializerMethodField()
    class Meta:
        model = models.JobPostProposal
        fields = [
        "pk", "job_post","message","proposal_sender","proposal_send_date",
        "proposal_sender_object"
        ]

    def get_proposal_sender_object(self,obj):
        business_page_rating = obj.proposal_sender.pro_business_profile.pro_business_review.all().aggregate(Avg('recommendation_rating')).get('recommendation_rating__avg', 0.00)
        business_page_object = {
            "pk":obj.proposal_sender.pro_business_profile.pk,
            "user":obj.proposal_sender.pro_business_profile.user.username,
            "professional_category":obj.proposal_sender.pro_business_profile.professional_category.category_name,
            "business_profile_image":obj.proposal_sender.pro_business_profile.business_profile_image.url if obj.proposal_sender.pro_business_profile.business_profile_image else '',
            "business_name":obj.proposal_sender.pro_business_profile.business_name,
            "phone":obj.proposal_sender.pro_business_profile.phone,
            "business_email":obj.proposal_sender.pro_business_profile.business_email,
            "pro_average_rating":business_page_rating if business_page_rating else '0'
        }

        user_object = {
            'pk':obj.proposal_sender.pk,
            'username':obj.proposal_sender.username,
            'first_name':obj.proposal_sender.first_name,
            'last_name':obj.proposal_sender.last_name,
            'email':obj.proposal_sender.email,
            'user_type':obj.proposal_sender.user_type,
            'profile_image':obj.proposal_sender.profile_image.url if obj.proposal_sender.profile_image else '',
            'business_page':business_page_object

            }
        return user_object


class JobPostSerializer(serializers.ModelSerializer):
    job_post_proposal = JobPostProposalSerializer(many=True, required=False)
    job_poster_object = serializers.SerializerMethodField()
    job_viewers_object = serializers.SerializerMethodField()
    class Meta:
        model = models.JobPost
        fields = [
        "pk", "title", "description", "project_size", "project_duration",
        "skill_areas", "verified", "active", "location", "job_viewers",
        "job_creation_date", "job_update_date","job_poster","job_poster_object",
        "job_viewers_object", "job_post_proposal"
        ]

    def get_job_poster_object(self,obj):
        user_object = {
            'pk':obj.job_poster.pk,
            'username':obj.job_poster.username,
            'first_name':obj.job_poster.first_name,
            'last_name':obj.job_poster.last_name,
            'email':obj.job_poster.email,
            'user_type':obj.job_poster.user_type,
            'profile_image':obj.job_poster.profile_image.url if obj.job_poster.profile_image else '',
            }
        return user_object

    def get_job_viewers_object(self,obj):
        user_array = []
        for usr in obj.job_viewers.all():
            user_object = {
                'pk':usr.pk,
                'username':usr.username,
                'first_name':usr.first_name,
                'last_name':usr.last_name,
                'email':usr.email,
                'user_type':usr.user_type,
                'profile_image':usr.profile_image.url if usr.profile_image else '',
                }
            user_array.append(user_object)
        return user_array

class JobPostViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobPost
        fields = ['job_viewers']
