import argparse
import sys
import subprocess
import os

path_vagrant = '~/self_monitor_vagrant'
path_ansible = '~/self-monitor'
o_s = 'ubuntu/bionic64'
private_key = '.vagrant/machines/default/virtualbox/private_key'
vagrantfile = f'{os.path.expanduser(path_vagrant)}/Vagrantfile'

parser = argparse.ArgumentParser()
parser.add_argument("argument", choices=['Init', 'Start', 'Stop', 'Destroy'], type=str, help="Init Stop Start Destroy")

def cmd(command_line):
    command_output = subprocess.check_output(f'{command_line}', shell=True).decode("utf8").split("\n")
    for line in command_output:
        print(line)

def init():
    cmd(f'mkdir -p {path_vagrant}; cd {path_vagrant}; rm -rf Vagrantfile; vagrant box add {o_s}; '
        f'vagrant init {o_s}; vagrant up')
    with open(vagrantfile) as f:
        l_line = f.readlines()
    l_line.insert(-1, 'config.vm.network "forwarded_port", guest: 80, host: 80\n'
                      'config.vm.network "forwarded_port", guest: 443, host: 443\n')
    with open(vagrantfile, 'w') as f:
        f.writelines(l_line)
    cmd(f'cd {path_vagrant}; vagrant reload')
    cmd('ansible-galaxy collection install community.mysql')
    cmd(f'cd {path_ansible}; ansible-playbook -i hosts --private-key {path_vagrant}/{private_key} Install_Env.yml 1>&2')
    print("use the following link https://localhost/grafana/d/z80i2GK7z/my_bord?orgId=1")

def start():
    cmd(f'cd {path_vagrant}; vagrant up')

def stop():
    cmd(f'cd {path_vagrant}; vagrant halt')

def destroy():
    cmd(f'cd {path_vagrant}; vagrant destroy -f; rm -rf {path_vagrant}; rm -rf ../self-monitor')

arguments = {
    'Init': getattr(sys.modules[__name__], 'init'),
    'Start': getattr(sys.modules[__name__], 'start'),
    'Stop': getattr(sys.modules[__name__], 'stop'),
    'Destroy': getattr(sys.modules[__name__], 'destroy')
}

if __name__ == '__main__':
    args = parser.parse_args()
    arguments[args.argument]()
