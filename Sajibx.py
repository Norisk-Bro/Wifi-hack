import sys
import os

try:
    import wifihack
    # যদি wifihack ফাইলের ভেতরে রান করার জন্য কোনো নির্দিষ্ট ফাংশন বা স্টার্ট কমান্ড থাকে তা এখানে দিতে হবে
    # যেমন অনেক টুলসে wifihack.main() বা অনুরূপ ফাংশন থাকে
    if hasattr(wifihack, 'main'):
        wifihack.main()
except Exception as e:
    print(f"Error loading module: {e}")
