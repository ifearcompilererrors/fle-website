from django.shortcuts import render_to_response
import settings
import pygeoip

gic = pygeoip.GeoIP('/usr/share/GeoIP/GeoIPCity.dat')

def landingpage(request):
	return render_to_response("landing_page.html")

def about(request):
	return render_to_response("about.html")

def involved(request):
	return render_to_response("involved.html")

def map(request):    
    ips = open(settings.PROJECT_PATH + "/ips.txt").readlines()
    records = [gic.record_by_addr(item.strip()) for item in ips if item]
    lat_lng = [(record['latitude'], record['longitude']) for record in records if record]
    # remove duplicates and remove null coordinates
    lat_lng = list(set(lat_lng) - set([(0, 0)]))
    return render_to_response('map.html', {"latlng": lat_lng})

