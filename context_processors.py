# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps
from django.conf import settings
from django.core.urlresolvers import reverse, NoReverseMatch
from django.shortcuts import resolve_url


def admin_sidebar_content(request):

    if not request.path.startswith(reverse('admin:index')):
        return {}

    items = []
    already_active = False
    for item in settings.SU_ADMIN_MENU:
        it = {
            'label': item['label'] if 'label' in item else None,
            'icon': item['icon'] if 'icon' in item else None,
            'active': False,
        }
        if 'model' in item:
            try:
                model = apps.get_model(*item['model'].rsplit('.', 1))
            except LookupError:
                continue

            try:
                it['url'] = reverse('admin:{}_{}_changelist'.format(*item['model'].rsplit('.', 1)))
            except NoReverseMatch:
                continue

            if not it['label']:
                # noinspection PyProtectedMember
                it['label'] = model._meta.verbose_name_plural

            if request.path.startswith(it['url']) and not already_active:
                it['active'] = True
                already_active = True
        elif 'items' in item:
            it['sub'] = []
            sub_already_active = False
            for subitem in item['items']:
                subit = {
                    'label': subitem['label'] if 'label' in subitem else None,
                    'icon': subitem['icon'] if 'icon' in subitem else None,
                    'active': False,
                }
                try:
                    model = apps.get_model(*subitem['model'].rsplit('.', 1))
                except LookupError:
                    continue

                try:
                    subit['url'] = reverse('admin:{}_{}_changelist'.format(*subitem['model'].rsplit('.', 1)))
                except NoReverseMatch:
                    continue

                if request.path.startswith(subit['url']) and not sub_already_active:
                    subit['active'] = True
                    sub_already_active = True
                    it['active'] = True
                    already_active = True

                if not subit['label']:
                    # noinspection PyProtectedMember
                    subit['label'] = model._meta.verbose_name_plural

                it['sub'].append(subit)

            if not it['sub']:
                continue
            else:

                it['url'] = it['sub'][0]['url']
        elif 'url' in item:
            it['url'] = resolve_url(item['url'])
            it['active'] = request.path == it['url'] and not already_active
            already_active = already_active or it['active']

        if it['icon'] is None:
            it['icon'] = "fa fa-angle-double-right"

        elif it['icon'].startswith('fa-'):
            it['icon'] = "fa " + it['icon']
        else:
            it['icon'] = "fa fa-" + it['icon']

        items.append(it)

    return {
        'su_admin_menu': items,
    }
