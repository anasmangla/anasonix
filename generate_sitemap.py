import glob
import datetime

urls = glob.glob('*.html')
now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S+00:00')
with open('sitemap.xml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url in urls:
        f.write('  <url>\n')
        f.write(f'    <loc>https://www.anasonix.com/{url}</loc>\n')
        f.write(f'    <lastmod>{now}</lastmod>\n')
        f.write('    <changefreq>monthly</changefreq>\n')
        f.write('    <priority>0.8</priority>\n')
        f.write('  </url>\n')
    f.write('</urlset>\n')
