# coding: utf-8

from django.db.models.signals import post_save, pre_save
from itertools import chain
from uuid import uuid4

from . import models
from main import models as edd_models


def campaign_check(sender, instance, raw, using, **kwargs):
    # don't do anything for raw loads from fixtures
    if not raw:
        # make sure there is a UUID set
        if instance.uuid is None:
            instance.uuid = uuid4()
        # log update, make sure created is set
        update = edd_models.Update.load_update()
        if instance.created_id is None:
            instance.created = update
        instance.updated = update
        # make sure there is a slug
        if instance.slug is None:
            instance.slug = instance._build_slug()


# ensure that signal is only connected once if this code runs again
dispatch = f"{campaign_check.__name__}:{models.Campaign.__name__}"
pre_save.connect(campaign_check, sender=models.Campaign, dispatch_uid=dispatch)


def campaign_update(sender, instance, raw, using, **kwargs):
    # don't do anything for raw loads from fixtures
    if not raw:
        # m2m relation must have IDs on both sides; has to be post_save
        instance.updates.add(instance.updated)


# ensure that signal is only connected once if this code runs again
dispatch = f"{campaign_update.__name__}:{models.Campaign.__name__}"
post_save.connect(campaign_update, sender=models.Campaign, dispatch_uid=dispatch)


def study_campaign_changed(sender, instance, raw, using, **kwargs):
    # when change is made adding link campaign-study, apply all campaign permissions to study
    q = dict(campaign_id=instance.campaign_id)
    permissions = chain(
        models.UserPermission.objects.filter(**q),
        models.GroupPermission.objects.filter(**q),
        models.EveryonePermission.objects.filter(**q),
    )
    for p in permissions:
        p.apply_to_study(instance.study)


# ensure that signal is only connected once if this code runs again
dispatch = f"{study_campaign_changed.__name__}:{models.CampaignMembership}"
post_save.connect(
    study_campaign_changed, sender=models.CampaignMembership, dispatch_uid=dispatch
)
