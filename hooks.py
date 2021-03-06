import dredd_hooks as hooks
import sys

# HELPERS
# NOTE move in separated module
import os
import sys
sys.path.append("/opt/xos")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xos.settings")
import django
from core.models import *
from services.cord.models import *
from services.vtr.models import *
import urllib2
import json
django.setup()


def doLogin(username, password):
    url = "http://127.0.0.1:8000/xoslib/login?username=%s&password=%s" % (username, password)
    res = urllib2.urlopen(url).read()
    parsed = json.loads(res)
    return {'token': parsed['xoscsrftoken'], 'sessionid': parsed['xossessionid']}


def cleanDB():
    # deleting all subscribers
    for s in CordSubscriberRoot.objects.all():
        s.delete(purge=True)

    # deleting all slices
    for s in Slice.objects.all():
        s.delete(purge=True)

    # deleting all Services
    for s in Service.objects.all():
        s.delete(purge=True)

    # deleting all Tenants
    for s in Tenant.objects.all():
        s.delete(purge=True)

    # deleting all Networks
    for s in Network.objects.all():
        s.delete(purge=True)

    # deleting all NetworkTemplates
    for s in NetworkTemplate.objects.all():
        s.delete(purge=True)

    for s in NetworkSlice.objects.all():
        s.delete(purge=True)

    for s in AddressPool.objects.all():
        s.delete(purge=True)

    # print 'DB Cleaned'


def createTestSubscriber():

    cleanDB()

    # load user
    user = User.objects.get(email="padmin@vicci.org")

    # network template
    private_template = NetworkTemplate()
    private_template.name = 'Private Network'
    private_template.save()

    # creating the test subscriber
    subscriber = CordSubscriberRoot(name='Test Subscriber 1', id=1)
    subscriber.save()

    # vRouter service
    vrouter_service = VRouterService()
    vrouter_service.name = 'service_vrouter'
    vrouter_service.save()

    # address pools
    ap_vsg = AddressPool()
    ap_vsg.service = vrouter_service
    ap_vsg.name = 'addresses_vsg'
    ap_vsg.addresses = '10.168.0.0'
    ap_vsg.gateway_ip = '10.168.0.1'
    ap_vsg.gateway_mac = '02:42:0a:a8:00:01'
    ap_vsg.save()

    # print 'vRouter created'

    # Site
    site = Site.objects.get(name='MySite')

    # vSG service
    vsg_service = VSGService()
    vsg_service.name = 'service_vsg'

    # vSG slice
    vsg_slice = Slice()
    vsg_slice.name = site.login_base + "_testVsg"
    vsg_slice.service = vsg_service.id
    vsg_slice.site = site
    vsg_slice.caller = user

<<<<<<< HEAD
    vsg_slice.save()

    vsg_service.save()

    # volt service
    volt_service = VOLTService()
    volt_service.name = 'service_volt'
    volt_service.save()

    # vcpe slice
    vcpe_slice = Slice()
    vcpe_slice.name = site.login_base + "_testVcpe"
    vcpe_slice.service = Service.objects.get(kind='vCPE')
    vcpe_slice.site = site
    vcpe_slice.caller = user
    vcpe_slice.save()

    # print 'vcpe_slice created'

    # create a lan network
    lan_net = Network()
    lan_net.name = 'lan_network'
    lan_net.owner = vcpe_slice
    lan_net.template = private_template
    lan_net.save()

    # print 'lan_network created'

    # add relation between vcpe slice and lan network
    vcpe_network = NetworkSlice()
    vcpe_network.network = lan_net
    vcpe_network.slice = vcpe_slice
    vcpe_network.save()

    # print 'vcpe network relation added'

    # vbng service
    vbng_service = VBNGService()
    vbng_service.name = 'service_vbng'
    vbng_service.save()

    # print 'vbng_service creater'

    # volt tenant
    vt = VOLTTenant(subscriber=subscriber.id, id=1)
    vt.s_tag = "222"
    vt.c_tag = "432"
    vt.provider_service_id = volt_service.id
    vt.caller = user
    vt.save()

    # print "Subscriber Created"


def deleteTruckrolls():
    for s in VTRTenant.objects.all():
        s.delete(purge=True)


def setUpTruckroll():
    service_vtr = VTRService()
    service_vtr.name = 'service_vtr'
    service_vtr.save()


def createTruckroll():
    setUpTruckroll()
    tn = VTRTenant(id=1)
    tn.save()


@hooks.before_all
def my_before_all_hook(transactions):
    # print "-------------------------------- Before All Hook --------------------------------"
=======
@hooks.before_all
def my_before_all_hook(transactions):
    print "-------------------------------- Before All Hook --------------------------------"
>>>>>>> 4523dc840d17b426f3e8a6be9ab0d7bd5ed65374
    cleanDB()


@hooks.before_each
def my_before_each_hook(transaction):
<<<<<<< HEAD
    # print "-------------------------------- Before Each Hook --------------------------------"
    # print transaction['name']
=======
    print "-------------------------------- Before Each Hook --------------------------------"
>>>>>>> 4523dc840d17b426f3e8a6be9ab0d7bd5ed65374
    auth = doLogin('padmin@vicci.org', 'letmein')
    transaction['request']['headers']['X-CSRFToken'] = auth['token']
    transaction['request']['headers']['Cookie'] = "xossessionid=%s; xoscsrftoken=%s" % (auth['sessionid'], auth['token'])
    createTestSubscriber()
    sys.stdout.flush()


@hooks.before("Truckroll > Truckroll Collection > Create a Truckroll")
def test1(transaction):
    setUpTruckroll()


@hooks.before("Truckroll > Truckroll Detail > View a Truckroll Detail")
def test2(transaction):
    deleteTruckrolls()
    createTruckroll()


@hooks.before("Truckroll > Truckroll Detail > Delete a Truckroll Detail")
def test3(transaction):
    deleteTruckrolls()
    createTruckroll()


@hooks.before("vOLT > vOLT Collection > Create a vOLT")
def test4(transaction):
    # transaction['skip'] = True
    VOLTTenant.objects.get(kind='vOLT').delete()
<<<<<<< HEAD


@hooks.before("Example > Example Services Collection > List all Example Services")
def exampleTest(transaction):
    transaction['skip'] = True
=======
>>>>>>> 4523dc840d17b426f3e8a6be9ab0d7bd5ed65374
