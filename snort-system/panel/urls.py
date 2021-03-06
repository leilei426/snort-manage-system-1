from django.conf.urls import patterns, url
from django.contrib import admin
from views import *


urlpatterns = patterns(
    '', url(r'^$', register, name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login'),
    url(r'^backstage/$', backstage, name='backstage'),
    url(r'^backstage/progress$', ProgressBar.as_view()),
    url(r'^backstage/rules/$', Show.as_view()),
    url(r'^backstage/log/$', LogShow.as_view()),
    url(r'^backstage/about/$', About.as_view()),
    url(r'^backstage/log/delete$', delete, name='delete'),
    url(r'^backstage/shield$', Shield.as_view()),
    url(r'^backstage/edit$', Edit.as_view()),
    url(r'^backstage/conflict$', ConflictShow.as_view()),
    url(r'^backstage/conflict/deal$', deal, name='deal'),
    url(r'^backstage/conflict/deal_conflict$',
        deal_conflict, name='deal_conflict'),
    url(r'^backstage/untranslate/$', Untranslate.as_view()),
    url(r'^backstage/untranslate/translate_show$',
        translate_show, name='translate_show'),
    url(r'^backstage/untranslate/trans_submit$',
        trans_submit, name='trans_submit'),
    url(r'^backstage/untranslate/untrans_search$',
        untrans_search, name='untrans_search'),
    url(r'^backstage/untranslate/untrans_result$',
        untrans_result, name='untrans_result'),
    url(r'^backstage/rules/detail$', detail_show, name='detail_show'),
    url(r'^backstage/rules/search$', search, name='search'),
    url(r'^backstage/rules/result$', search_result, name='search_result'),
    url(r'^backstage/rules/add$', Add.as_view()),
    url(r'^backstage/rules/add_submit$', add_submit, name='add_submit'),
    url(r'^backstage/rules/shield$', shield, name='shield'),
    url(r'^backstage/rules/edit$', edit, name='edit'),
    url(r'^backstage/rules/in$', rules_in, name='rules_in'),
    url(r'^backstage/logout/$', logout, name='logout'),
    url(r'^backstage/upload$', Upload.as_view()),
    url(r'^backstage/download$', Download.as_view()),
    url(r'^backstage/xlsx$', Xlsx.as_view()),
    url(r'^backstage/download_pcap$', DownloadPcap.as_view()),
    url(r'^backstage/delete_pcap$', DeletePcap.as_view()),
    url(r'^backstage/upload/file$', upload, name='upload'),
    url(r'^backstage/xlsx/file$', get_xlsx, name='get_xlsx'),
    url(r'^backstage/download/file$', download, name='download'),
    url(r'^backstage/download/pcap$', download_pcap, name='download_pcap'),
    url(r'^backstage/delete/pcap$', pcap_delete, name='pcap_delete'),
    url(r'^backstage/log/detail$', log_detail, name='log_detail'),
    url(r'^backstage/add/content$', add_content, name='add_content'),
    url(r'^backstage/rules/export$', time_export, name='time_export'),
    url(r'^backstage/rules/complete$', complete_show, name='complete_show'),
    url(r'^backstage/rules/custom/export$',
        custom_export, name='custom_export'),
    url(r'^backstage/pcap/verify$', hit_pcap_rule, name='hit_pcap_rule'),
    url(r'^backstage/upload/pcap$', PcapUpload.as_view()),
    url(r'^backstage/upload/local$', LocalRuleUpload.as_view()),
    url(r'^backstage/local/import$', import_local_rule, name='import_local_rule')
)
