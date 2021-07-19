import re
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Generates a list of videos on hololivevideos.download that are not available on youtube for a specific channel')
parser.add_argument('html_file', help='The HTML file retreived for a channel from hololivevideos.download')
parser.add_argument('channel_ids', help='A list of youtube video ids retrieved with youtube-dl from the channel of interest')
parser.add_argument('--url_output', '-u', help='File to output the url for each of the videos found with this tool')
args = parser.parse_args()
print(args)
df = pd.read_html(args.html_file)[0]
df.columns = ['Title', 'Date', 'Runtime', 'Size', 'Youtube ID']
hd_titles = df['Title']
hd_ids = df['Youtube ID']


ids = []
with open(args.channel_ids, 'r') as titlefile:
    for line in titlefile:
        ch_id = line.strip()
        ids.append(ch_id)

channel_ids = pd.Series(ids)
print(channel_ids[0:5])
print(type(channel_ids))
print(hd_ids[0:5])
print(type(hd_ids))

print('\n')
print(hd_ids.isin(channel_ids))
not_available_ids = hd_ids[~hd_ids.isin(channel_ids)]
not_available_titles = hd_titles[~hd_ids.isin(channel_ids)]
not_available_sizes = df['Size'][~hd_ids.isin(channel_ids)]

size_regex = re.compile('([0-9.]+) ([MG]B)')
def convert_size(size):
    res = size_regex.match(size)
    if not res:
        return 0
    number = float(res.group(1))
    suffix = res.group(2)
    if suffix == 'GB':
        number *= 1024
    return number

sizes = map(convert_size, not_available_sizes)
total_size = sum(sizes)
    
print('List of videos found that are not on Youtube:')
print('"Youtube ID", "Title", size')
for vid_id, title, size in zip(not_available_ids, not_available_titles, not_available_sizes):
    print(f'"{vid_id}", "{title}", {size}')

print(f'Total download size: {total_size:.2f} MB - {total_size/1024:.2f} GB')

if args.url_output:
    with open(args.url_output, 'w') as urlfile:
        for vid_id in not_available_ids:
            urlfile.write(f'https://hololivevideos.download/dl/{vid_id}.mp4\n')
    
