import re,sys
src=open(sys.argv[1]).read()
body=open('body.html').read(); css=open('extra.css').read()
a=src.find('<main id="brx-content">'); b=src.find('</main>')
out=src[:a]+'<main id="brx-content">'+body+src[b:]
out=out.replace('bricks-lazy-hidden','')
out=out.replace('</head>','<style>'+css+'</style></head>',1)
out=re.sub(r'<title>.*?</title>','<title>HVAC Google Ads &amp; LSAs → Bid on Installs, Not Clicks</title>',out,1,flags=re.S)
out=out.replace('<head>','<head><base href="https://andrewryanmarketing.com/">',1)
open('ppc-mockup.html','w').write(out)
