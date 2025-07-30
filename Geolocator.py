
import re;
from math import sin, cos, sqrt, asin, radians  

# Extracting coordinates from the urls
def extract_coordinates(url):
  match = re.search(r'q=(-?\d+\.\d+),(-?\d+\.\d+)',url)
  if match:
    lat,long = match.groups()
    return float(lat),float(long)
  
  else:
    return None



url=[
  
  "http://maps.google.com/maps?q=-8.139957,36.669067",
  "http://maps.google.com/maps?q=-8.139395,36.667262",
  "http://maps.google.com/maps?q=-8.140880,36.669692",
  "http://maps.google.com/maps?q=-8.140160,36.673127",
  "http://maps.google.com/maps?q=-8.139172,36.671658",
  "http://maps.google.com/maps?q=-8.136200,36.671653",
  "http://maps.google.com/maps?q=-8.137592,36.668663",
  "http://maps.google.com/maps?q=-8.138105,36.665122",
  "http://maps.google.com/maps?q=-8.136673,36.664277",
	"http://maps.google.com/maps?q=-8.134107,36.669272",
	"http://maps.google.com/maps?q=-8.135458,36.669505",
	"http://maps.google.com/maps?q=-8.132137,36.667622",
	"http://maps.google.com/maps?q=-8.130203,36.669497",
	"http://maps.google.com/maps?q=-8.127067,36.668128",
	"http://maps.google.com/maps?q=-8.123668,36.667347",
	"http://maps.google.com/maps?q=-8.125780,36.671785",
	"http://maps.google.com/maps?q=-8.143873,36.669253",
	"http://maps.google.com/maps?q=-8.143833,36.671365",
	"http://maps.google.com/maps?q=-8.142767,36.672702",
	"http://maps.google.com/maps?q=-8.147755,36.669503",
	"http://maps.google.com/maps?q=-8.152952,36.668628",
	"http://maps.google.com/maps?q=-8.156255,36.668505",
	"http://maps.google.com/maps?q=-8.160650,36.671715",
	"http://maps.google.com/maps?q=-8.144422,36.667467",
	"http://maps.google.com/maps?q=-8.147400,36.665492",
	"http://maps.google.com/maps?q=-8.145208,36.664078",
	"http://maps.google.com/maps?q=-8.147040,36.659953",
	"http://maps.google.com/maps?q=-8.143230,36.661803",
	"http://maps.google.com/maps?q=-8.141515,36.666305",
	"http://maps.google.com/maps?q=-8.140587,36.658875",
	"http://maps.google.com/maps?q=-8.136455,36.658388",
	"http://maps.google.com/maps?q=-8.139548,36.653478",
	"http://maps.google.com/maps?q=-8.144478,36.655602",
	"http://maps.google.com/maps?q=-8.147410,36.652363",
	"http://maps.google.com/maps?q=-8.152707,36.651180",
	"http://maps.google.com/maps?q=-8.150900,36.647652",
	"http://maps.google.com/maps?q=-8.148530,36.646268",
	"http://maps.google.com/maps?q=-8.144678,36.637868",
	"http://maps.google.com/maps?q=-8.140962,36.640400",
	"http://maps.google.com/maps?q=-8.141990,36.646127",
	"http://maps.google.com/maps?q=-8.143410,36.653258",
	"http://maps.google.com/maps?q=-8.131433,36.645023",
	"http://maps.google.com/maps?q=-8.135677,36.684902",
	"http://maps.google.com/maps?q=-8.137013,36.682980",
	"http://maps.google.com/maps?q=-8.141285,36.678193",
	"http://maps.google.com/maps?q=-8.144160,36.677210",
	"http://maps.google.com/maps?q=-8.142142,36.675993",
	"http://maps.google.com/maps?q=-8.145570,36.679647",
	"http://maps.google.com/maps?q=-8.145517,36.676767",
	"http://maps.google.com/maps?q=-8.146768,36.679448",
	"http://maps.google.com/maps?q=-8.129183,36.675567",
	"http://maps.google.com/maps?q=-8.130155,36.672007",
	"http://maps.google.com/maps?q=-8.133372,36.679662",
	"http://maps.google.com/maps?q=-8.130972,36.678855",
	"http://maps.google.com/maps?q=-8.129975,36.682730",
	"http://maps.google.com/maps?q=-8.131968,36.681990",
	"http://maps.google.com/maps?q=-8.118925,36.683908",
	"http://maps.google.com/maps?q=-8.116562,36.679538",
	"http://maps.google.com/maps?q=-8.120550,36.679447",
	"http://maps.google.com/maps?q=-8.122098,36.676527",
	"http://maps.google.com/maps?q=-8.124397,36.679233",
	"http://maps.google.com/maps?q=-8.126647,36.682575",
	"http://maps.google.com/maps?q=-8.128315,36.679375",
	"http://maps.google.com/maps?q=-8.128490,36.674502",
	"http://maps.google.com/maps?q=-8.125600,36.675210",
	"http://maps.google.com/maps?q=-8.131977,36.686692",
  "http://maps.google.com/maps?q=-8.134617,36.685012",
	"http://maps.google.com/maps?q=-8.132918,36.689125",
	"http://maps.google.com/maps?q=-8.124133,36.692170",
	"http://maps.google.com/maps?q=-8.125605,36.690605",
	"http://maps.google.com/maps?q=-8.126608,36.688118",
	"http://maps.google.com/maps?q=-8.128225,36.691750",
	"http://maps.google.com/maps?q=-8.124018,36.693452",
	"http://maps.google.com/maps?q=-8.128393,36.697120",
	"http://maps.google.com/maps?q=-8.125473,36.684022",
	"http://maps.google.com/maps?q=-8.121328,36.685928",
	"http://maps.google.com/maps?q=-8.129655,36.684675",
	"http://maps.google.com/maps?q=-8.095190,36.598950",
	"http://maps.google.com/maps?q=-8.094030,36.596088",
	"http://maps.google.com/maps?q=-8.091442,36.584242",
	"http://maps.google.com/maps?q=-8.088058,36.565937",
	"http://maps.google.com/maps?q=-8.089595,36.571963",
	"http://maps.google.com/maps?q=-8.095883,36.576907",
	"http://maps.google.com/maps?q=-8.090447,36.579365",
	"http://maps.google.com/maps?q=-8.095608,36.605252",
	"http://maps.google.com/maps?q=-8.101590,36.610892",
	"http://maps.google.com/maps?q=-8.141377,36.704998",
	"http://maps.google.com/maps?q=-8.149758,36.695585",
	"http://maps.google.com/maps?q=-8.145618,36.692782",
	"http://maps.google.com/maps?q=-8.145273,36.698802",
	"http://maps.google.com/maps?q=-8.164807,36.681247",
	"http://maps.google.com/maps?q=-8.160658,36.684770",
	"http://maps.google.com/maps?q=-8.152370,36.683132",
	"http://maps.google.com/maps?q=-8.155903,36.680252",
	"http://maps.google.com/maps?q=-8.147608,36.680870",
	"http://maps.google.com/maps?q=-8.147742,36.685317",
	"http://maps.google.com/maps?q=-8.151388,36.689433",
	"http://maps.google.com/maps?q=-8.140122,36.695068"

]

locations = []

for links in url:
  coords = extract_coordinates(links)
  if coords:
    lat,long = coords
    locations.append({"lat":lat,"long":long}) 


#Use the haversine function to calculate the shortest distance between points on a sphere

def haversine(lat1,lng1,lat2,lng2):
  lat1,lng1,lat2,lng2 = map(radians,[lat1,lng1,lat2,lng2])
  R=6370
  dlat=lat2-lat1
  dlng=lng2-lng1

  a = sin(dlat/2)**2 + cos(lng1)*cos(lng2)*sin(dlng/2)**2
  distance = 2*R*asin(sqrt(a))
  return distance

# Function that shows the 50 selected locations based on the minimum distance of 500m

def select_far_locations (locations,min_distance=0.50,limit=50):
  selected=[]
  for loc in locations:
    if len(selected)>=limit:
      break

    too_close = False

    for sel in selected:
      dist = haversine(loc['lat'],loc['long'],sel['lat'],sel['long'])
      if dist<min_distance:
        too_close = True
        break

    if not too_close:
      selected.append(loc)
      

  return selected 

def extracting_urls(selected,urls):
  selected_urls=[]
  for i, url in enumerate(urls):
    for sel in selected:
      if(str(sel['lat'])in urls[i] and str(sel['long'])in urls[i] ):
        selected_urls.append(urls[i])
        break

  return selected_urls

# Step 1: Get selected coordinates
selected = select_far_locations(locations)

# Step 2: Generate JavaScript object
print("const points = {")
for i, loc in enumerate(selected, 1):  # start index at 1 for point labels
    print(f"  {i}: [{loc['lat']}, {loc['long']}],")
print("};")


pairs = []
for i in range(len(selected)):
    for j in range(i+2, len(selected)):
        dist = haversine(selected[i]['lat'], selected[i]['long'],
                         selected[j]['lat'], selected[j]['long'])
        if dist >= 0.5:
            pairs.append((i+1, j+1, dist))  # i+1 so IDs match JS

# Export to JS
print("const pairs = [")
for a, b, d in pairs:
    print(f"  [{a}, {b}, {d:.3f}],")
print("];")


    





  





