import re
from os import popen, system

output = popen("xinput | grep 'DELL081A:00 044E:120A Touchpad'").read()
device_match = re.search(r"id=(\d+)", output)

if device_match:
    device = device_match.group(1)

    natural_props_raw = popen(f'xinput list-props {device} | grep "Natural Scrolling Enabled ("').read()
    natural_scrolling_match = re.search(r'((\d+))', natural_props_raw)
    
    if natural_scrolling_match:
        natural_scrolling_prop = natural_scrolling_match.group(0)
        system(f"xinput set-prop {device} --type=int --format=8 {natural_scrolling_prop} 1")
    else:
        print("Natural Scrolling property not found.")

    tapping_props_raw = popen(f'xinput list-props {device} | grep "Tapping Enabled ("').read()
    tapping_match = re.search(r'((\d+))', tapping_props_raw)

    if tapping_match:
        tapping_prop = tapping_match.group(0)
        system(f"xinput set-prop {device} --type=int --format=8 {tapping_prop} 1")
    else:
        print("Tapping property not found.")
else:
    print("Touchpad device not found.")
