#!/usr/bin/env python
import pexpect as p
import subprocess
import time
import sys


subprocess.call(['qemu-img', 'create', '-f', 'qcow2', 'image_file', '7G'])


PS1 = '12345'

# c = p.spawn('qemu-system-x86_64 -cdrom archlinux-2022.10.01-x86_64.iso'
#             ' -boot order=d -drive file=image_file,format=qcow2 -m 3G'
#             ' -accel kvm -nographic'
#             ' -cpu host,hv_relaxed,hv_spinlocks=0x1fff,hv_vapic,hv_time'
#             ' -smp 12', encoding='utf-8', logfile=sys.stdout)

c = p.spawn('qemu-system-x86_64 -cdrom archlinux-2022.10.01-x86_64.iso'
            ' -boot order=d -drive file=image_file,format=qcow2 -m 3G'
            ' -accel kvm -nographic'
            ' -cpu host,hv_relaxed,hv_spinlocks=0x1fff,hv_vapic,hv_time'
            ' -smp 12')



c.expect('.*Automatic.*')
time.sleep(0.4)
c.send('\t')
c.sendline(' console=ttyS0')
time.sleep(0.4)
c.sendline()
c.expect('archiso login: ')
c.sendline('root')
print('loged')
# time.sleep(25)

# could not set PS1 with zsh
c.sendline('bash')
c.sendline('PS1='+ PS1)

# Lets automate the pre chroot stage


# there is a systemd service that starts at boot and its called pacman-init that inits the keyring and populates it

# c.sendline('pacman -Sy --noconfirm git make')
# c.expect(PS1)
# # c.sendline('git clone git@github.com:Xein234/dotfiles.git /.dotfiles')
# # c.sendline('cd /.dotfiles')
# # c.sendline('git checkout sysqemu')
# # c.sendline('make prechroot')

#

serviceName = 'git-and-make.service'
with open(serviceName) as service:
    c.sendline('cat <<EOOF > /etc/systemd/system/' + serviceName)
    c.sendline("'" + service.read() + "'")
    c.sendline('EOOF')

c.sendline('systemctl daemon-reload')
c.sendline('systemctl start git-and-make')
# c.expect(PS1)


# for i in range(120):
#     c.sendline('systemctl is-active pacman-init.service')
#     try:
#         c.expect
#     except Exception as e:
#         raise e
#     sleep(1)

c.sendline()
c.interact()

# c.expect(prompt, timeout=180)

# c.sendline('git clone git@github.com:Xein234/dotfiles.git /.dotfiles')
# c.expect(prompt)

# c.sendline('parted -a optimal /dev/sda mklabel msdos mkpart primary ext4 0% 100%')
# c.sendline('mkfs.ext4 /dev/sda1')
# c.sendline('mount /dev/sda1 /mnt')
# start = time.time()
# c.sendline('pacstrap -K /mnt base linux linux-firmware')
# end = time.time()
# print(end - start)
#
