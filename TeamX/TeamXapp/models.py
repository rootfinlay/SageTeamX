#############################################
# References
from django.db import models
from django.core.exceptions import ValidationError
#############################################

###################################################################
# Class - decribes an instanance of a :-
# AllMembers      - person who can be a memeber of a scrum team
# ScrumTeam       - scrum developemnt team
# Skills          - skills relavant to a job role
# ScrumTeamRole   - job role a person has
# TODO rename class ScrumTeamRole to JobRole
# JobRoleGroup    - common name to group of job roles
# ScrumTeamType   - type of agile development team
# ScrumTeamStatus - scrum team status
# Domain          - a funtional / developent area
# LeaveStatus     - type of leave request
# TODO rename class LeaveStatus to LeaveType
# LeaveCalendar   - team memebers leave request
###################################################################

class Config(models.Model):
    class Meta:
        verbose_name = 'Some other name'


class AllMembers(models.Model):
    IN_TEAM_CHOICES = [('YES', 'Yes') , ('NO', 'No')]
    WORK_PATTERN_CHOICES = [('FULL TIME' , 'Full time') , ('PART TIME', 'Part time') , ('COMPRESSED HOURS', 'Compressed hours')]
    first_name = models.CharField(max_length=30, verbose_name="First name")
    second_name = models.CharField(max_length=30, verbose_name="Second name")
    work_pattern = models.CharField(choices=WORK_PATTERN_CHOICES, max_length=16, default='FULL TIME', null=True, blank=True)
    hours_per_week = models.IntegerField(verbose_name="Hours Per Week" , default=35)
    email = models.EmailField(null=True,blank=True)
    scrum_team_name = models.ForeignKey("ScrumTeam", on_delete=models.PROTECT, verbose_name="Scrum teams", null=True, blank=True)
    scrum_team_roles = models.ForeignKey("ScrumTeamRole", on_delete=models.DO_NOTHING, verbose_name="Roles", null=True, blank=True)
    myskill = models.ManyToManyField('Skills', blank=True, verbose_name="Skills")
    avatar = models.ImageField(null=True, blank=True)
    location = models.ForeignKey("location",on_delete=models.PROTECT, verbose_name="Location", null=True, blank=True)
    # in_team = models.CharField(choices=IN_TEAM_CHOICES, max_length=3, default='NO', null=True, blank=True, verbose_name="In team")

    def __str__ (self):
        return self.first_name + ' ' +  self.second_name

    def clean(self):
        if self.hours_per_week>35:
            raise ValidationError("Hours worked per week cannot be more than 35!")
        elif self.work_pattern=='FULL TIME' and self.hours_per_week<35:
            raise ValidationError("You need to work 35 hours per week to be able to be full time!")
        elif self.work_pattern=='PART TIME' and self.hours_per_week==35:
            raise ValidationError("You cannot work 35 hours as part time!")

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"


class ScrumTeam(models.Model):
    team_name = models.CharField(max_length=30, verbose_name="Scrum Team Name", null=True, blank=True)
    team_type = models.ForeignKey("ScrumTeamType", on_delete=models.PROTECT, null=True, blank=True, verbose_name="Team Type")
    current_focus = models.TextField(blank=True, null=True, verbose_name="Current Focus")
    scrum_master = models.ForeignKey("AllMembers", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="Scrum Master")
    team_status = models.ForeignKey("ScrumTeamStatus", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="Team Status")
    domain = models.ForeignKey('Domain', null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="Domain")

    def __str__ (self):
        return self.team_name

    class Meta:
        verbose_name = 'Scrum Team'
        verbose_name_plural = 'Scrum Teams'


class Skills(models.Model):

    skill = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class ScrumTeamRole(models.Model):
    name = models.CharField(max_length=30, verbose_name="Scrum Team Role:")
    job_role_group = models.ForeignKey("JobRoleGroup", null=True, blank=True, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Role'
        verbose_name_plural = 'Job Roles'


class JobRoleGroup(models.Model):
    name = models.CharField(max_length=50, verbose_name="Role Group")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Job Role Group"
        verbose_name_plural = "Job Role Groups"


class ScrumTeamType(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Scrum Team Type'
        verbose_name_plural = 'Scrum Team Types'


class ScrumTeamStatus(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Scrum Team Status'
        verbose_name_plural = 'Scrum Team Status'


class Domain(models.Model):
    domain_name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.domain_name

    class Meta:
        verbose_name = 'Domain'
        verbose_name_plural = 'Domains'


class LeaveStatus(models.Model):
    leave_status = models.CharField(max_length=31, null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.leave_status

    class Meta:
        verbose_name = 'Leave Type'
        verbose_name_plural = 'Leave Type'


class LeaveCalendar(models.Model):
    team_member = models.ForeignKey("AllMembers", on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    total_hours = models.IntegerField()
    leave_type = models.ForeignKey("LeaveStatus", on_delete=models.DO_NOTHING, null=True, blank=True)
    note = models.TextField(blank=True, null=True, verbose_name="Leave Note")

    def __str__(self):
        return str(self.team_member)

class location(models.Model):

    location_name = models.CharField(max_length=50, verbose_name="Location")
    country = models.CharField(max_length=100, verbose_name="Country")

    class Meta:
        verbose_name = ("Location")
        verbose_name_plural = ("Locations")

    def __str__(self):
        return self.location_name

    
