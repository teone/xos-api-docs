import dredd_hooks as hooks
import sys
import commands


restoreSubscriber = "ssh xos 'sudo docker exec frontend_xos_db_1 psql -U postgres -d xos -c \"UPDATE core_tenantroot SET deleted=false WHERE id=1;\"'"


@hooks.before_each
def my_before_each_hook(transaction):
    print('before each restore')
    commands.getstatusoutput(restoreSubscriber)
    sys.stdout.flush()
