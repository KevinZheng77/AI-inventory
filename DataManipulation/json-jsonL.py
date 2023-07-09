import json

def find_entity_in_text(entity, text):
    try:
        start_index = text.index(entity)
        end_index = start_index + len(entity)
        return start_index, end_index
    except ValueError:
        return None, None

def convert_json_to_jsonl(json_objects):
    with open('output.jsonl', 'w') as file:
        for data in json_objects:

            text = data.get('Text', '')
            entities = ['Name', 'Size', 'Cost', 'Selling']  # Add more if you need
            textSegmentAnnotations = []

            for entity in entities:
                value = data.get(entity, '')
                start, end = find_entity_in_text(value, text)
                if start is not None and end is not None:
                    textSegmentAnnotations.append({
                        "displayName": entity,
                        "startOffset": start,
                        "endOffset": end
                    })

            jsonl_data = {
                "textContent": text,
                "textSegmentAnnotations": textSegmentAnnotations
            }

            file.write(json.dumps(jsonl_data) + '\n')  # Write each JSONL line into the file

# Example array of JSON objects
json_objects = [
   {"Text":"Picked up Air Jordan 1 Retro High Pine Green in size 11 for $170 looking to sell for $220","Name":"Jordan 1 Retro High Pine Green","SKU":"none","Size":"11","Quantity":1,"Cost":"$170","Selling":"$220"},
{"Text":"Bought Yeezy Boost 350 V2 Zebra size 9. Cost price was $230 hope to sell for $270","Name":"Yeezy Boost 350 V2 Zebra","SKU":"none","Size":"9","Quantity":1,"Cost":"$230","Selling":"$270"},
{"Text":"Got a deal on Nike Dunk Low University Red in size 10 for $150 planning to sell for $200","Name":"Nike Dunk Low University Red","SKU":"none","Size":"10","Quantity":1,"Cost":"$150","Selling":"$200"},
{"Text":"Scored a pair of Air Jordan 4 Retro Fire Red size 12 for $190 listing them for $240","Name":"Jordan 4 Retro Fire Red","SKU":"none","Size":"12","Quantity":1,"Cost":"$190","Selling":"$240"},
{"Text":"Purchased Nike Dunk High Spartan Green in size 11.5 for $160 selling for $210","Name":"Nike Dunk High Spartan Green","SKU":"none","Size":"11.5","Quantity":1,"Cost":"$160","Selling":"$210"},
{"Text":"Managed to buy Yeezy Boost 700 Wave Runner size 10 for $300 reselling price is $350","Name":"Yeezy Boost 700 Wave Runner","SKU":"none","Size":"10","Quantity":1,"Cost":"$300","Selling":"$350"},
{"Text":"Found Adidas NMD_R1 Tokyo in size 9.5 for $140 will be sold for $190","Name":"Adidas NMD_R1 Tokyo","SKU":"none","Size":"9.5","Quantity":1,"Cost":"$140","Selling":"$190"},
{"Text":"Acquired Air Jordan 3 Retro UNC size 8 for $200 planning to sell for $250","Name":"Air Jordan 3 Retro UNC","SKU":"none","Size":"8","Quantity":1,"Cost":"$200","Selling":"$250"},
{"Text":"Bought New Balance 327 Primary Pack size 10.5 for $90 selling them for $140","Name":"New Balance 327 Primary Pack","SKU":"none","Size":"10.5","Quantity":1,"Cost":"$90","Selling":"$140"},
{"Text":"Just got Yeezy 450 Cloud White size 11 for $200 will be sold for $250","Name":"Yeezy 450 Cloud White ","SKU":"none","Size":"11","Quantity":1,"Cost":"$200","Selling":"$250"},
{"Text":"Found a pair of Air Jordan 5 Retro Fire Red in size 9 for $190 selling for $240","Name":"Air Jordan 5 Retro Fire Red","SKU":"none","Size":"9","Quantity":1,"Cost":"$190","Selling":"$240"},
{"Text":"Purchased Adidas UltraBoost 21 Triple Black in size 10 for $180 reselling for $230","Name":"Adidas UltraBoost 21 Triple Black","SKU":"none","Size":"10","Quantity":1,"Cost":"$180","Selling":"$230"},
{"Text":"Scored a Nike Air Force 1 07 White size 8.5 for $90 listing them for $140","Name":"Nike Air Force 1 07 White","SKU":"none","Size":"8.5","Quantity":1,"Cost":"$90","Selling":"$140"},
{"Text":"Managed to get Converse Chuck Taylor All-Star 70s Hi Off-White size 9 for $130 selling price is $180","Name":"Converse Chuck Taylor All-Star 70s","SKU":"none","Size":"9","Quantity":1,"Cost":"$130","Selling":"$180"},
{"Text":"Acquired Adidas Yeezy QNTM Barium in size 10.5 for $250 will be sold for $300","Name":"Yeezy QNTM Barium","SKU":"none","Size":"10.5","Quantity":1,"Cost":"$250","Selling":"$300"},
{"Text":"Bought Nike Air Max 97 Silver Bullet size 12 for $160 planning to resell for $210","Name":"Nike Air Max 97","SKU":"none","Size":"12","Quantity":1,"Cost":"$160","Selling":"$210"},
{"Text":"Picked up New Balance 992 Grey Day in size 9.5 for $180 selling for $230","Name":"New Balance 992 Grey Day","SKU":"none","Size":"9.5","Quantity":1,"Cost":"$180","Selling":"$230"},
{"Text":"Just got Adidas Stan Smith Green size 8 for $80 will be sold for $130","Name":"Adidas Stan Smith Green","SKU":"none","Size":"8","Quantity":1,"Cost":"$80","Selling":"$130"},
{"Text":"Scored a pair of Nike SB Dunk Low Shadow size 10 for $110 listing them for $160","Name":"Nike SB Dunk Low Shadow","SKU":"none","Size":"10","Quantity":1,"Cost":"$110","Selling":"$160"},
{"Text":"Found Vans Old Skool Black/White in size 11.5 for $60 planning to sell for $110","Name":"Vans Old Skool","SKU":"none","Size":"11.5","Quantity":1,"Cost":"$60","Selling":"$110"},
{"Text":"Bought Adidas Yeezy Boost 700 V2 Cream size 9.5 for $240 planning to sell for $290","Name":"Yeezy Boost 700 V2 Cream","SKU":"none","Size":"9.5","Quantity":1,"Cost":"$240","Selling":"$290"},
{"Text":"Acquired a pair of Converse One Star Golf le Fleur size 10 for $100 listing them for $150","Name":"Converse One Star Golf le Fleur","SKU":"none","Size":"10","Quantity":1,"Cost":"$100","Selling":"$150"},
{"Text":"Picked up Nike SB Dunk Low Grateful Dead Bears Orange size 11 for $300 selling for $350","Name":"Nike SB Dunk Low Grateful Dead Bears","SKU":"none","Size":"11","Quantity":1,"Cost":"$300","Selling":"$350"},
{"Text":"Managed to get Air Jordan 1 Retro High OG Obsidian in size 8.5 for $210 will be sold for $260","Name":"Jordan 1 Retro High OG Obsidian","SKU":"none","Size":"8.5","Quantity":1,"Cost":"$210","Selling":"$260"},
{"Text":"Scored a New Balance 992 Joe Freshgoods - Anatomy of a Heart size 10.5 for $270 selling price is $320","Name":"New Balance 992 Joe Freshgoods","SKU":"none","Size":"10.5","Quantity":1,"Cost":"$270","Selling":"$320"},
{"Text":"Purchased Yeezy Boost 380 Mist in size 9 for $230 hope to sell for $280","Name":"Yeezy Boost 380 Mist","SKU":"none","Size":"9","Quantity":1,"Cost":"$230","Selling":"$280"},
{"Text":"Just got Nike Air Max 90 Bacon size 12 for $140 looking to sell for $190","Name":"Nike Air Max 90 Bacon","SKU":"none","Size":"12","Quantity":1,"Cost":"$140","Selling":"$190"},
{"Text":"Found Adidas Superstar Run DMC My Adidas 50th Anniversary size 11.5 for $150 reselling price is $200","Name":"Adidas Superstar Run DMC My Adidas 50th Anniversary","SKU":"none","Size":"11.5","Quantity":1,"Cost":"$150","Selling":"$200"},
{"Text":"Bought Air Jordan 4 Retro Metallic Purple size 8 for $190 will be sold for $240","Name":"Jordan 4 Retro Metallic Purple","SKU":"none","Size":"8","Quantity":1,"Cost":"$190","Selling":"$240"},
{"Text":"Managed to buy Nike Air Force 1 Low Travis Scott size 10 for $250 selling them for $300","Name":"Nike Air Force 1 Low Travis Scott","SKU":"none","Size":"10","Quantity":1,"Cost":"$250","Selling":"$300"},
{"Text":"Scored a pair of Vans Slip-On Checkerboard in size 9.5 for $50 planning to sell for $100","Name":"Vans Slip-On Checkerboard","SKU":"none","Size":"9.5","Quantity":1,"Cost":"$50","Selling":"$100"},
{"Text":"Acquired Adidas Stan Smith Human Made size 11 for $130 listing them for $180","Name":"Adidas Stan Smith Human Made","SKU":"none","Size":"11","Quantity":1,"Cost":"$130","Selling":"$180"},
{"Text":"Purchased Yeezy 500 Blush in size 10.5 for $220 selling price is $270","Name":"Yeezy 500 Blush","SKU":"none","Size":"10.5","Quantity":1,"Cost":"$220","Selling":"$270"},
{"Text":"Got a deal on Nike Air Max 97 Sean Wotherspoon size 9 for $600 will be sold for $650","Name":"Nike Air Max 97 Sean Wotherspoon","SKU":"none","Size":"9","Quantity":1,"Cost":"$600","Selling":"$650"},
{"Text":"Bought Nike SB Dunk High Strawberry Cough size 10 for $200 planning to resell for $250","Name":"Nike SB Dunk High Strawberry Cough","SKU":"none","Size":"10","Quantity":1,"Cost":"$200","Selling":"$250"},
{"Text":"Just got Adidas UltraBoost 20 ISS National Lab - Dash Grey size 8.5 for $180 looking to sell for $230","Name":"Adidas UltraBoost 20 ISS National Lab - Dash Grey","SKU":"none","Size":"8.5","Quantity":1,"Cost":"$180","Selling":"$230"},
{"Text":"Scored a Air Jordan 1 Low Paris in size 12 for $210 reselling price is $260","Name":"Air Jordan 1 Low Paris","SKU":"none","Size":"12","Quantity":1,"Cost":"$210","Selling":"$260"},
{"Text":"Found New Balance 1300 Steel Blue size 11.5 for $220 selling for $270","Name":"New Balance 1300 Steel Blue","SKU":"none","Size":"11.5","Quantity":1,"Cost":"$220","Selling":"$270"},
{"Text":"Managed to buy Converse Chuck Taylor All-Star Comme des Garcons PLAY size 8 for $130 will be sold for $180","Name":"Converse Chuck Taylor All-Star Comme des Garcons PLAY","SKU":"none","Size":"8","Quantity":1,"Cost":"$130","Selling":"$180"},
{"Text":"Acquired Nike Dunk Low Ceramic in size 10.5 for $150 planning to sell for $200","Name":"Nike Dunk Low Ceramic","SKU":"none","Size":"10.5","Quantity":1,"Cost":"$150","Selling":"$200"},
{"Text":"Picked up Air Jordan 6 Retro DMP size 9.5 for $200 selling for $250","Name":"Air Jordan 6 Retro DMP","SKU":"none","Size":"9.5","Quantity":1,"Cost":"$200","Selling":"$250"},
{"Text":"Bought Nike SB Dunk Low Ben & Jerry Chunky Dunky size 11 for $1000 listing them for $1050","Name":"Nike SB Dunk Low Ben & Jerry Chunky Dunky","SKU":"none","Size":"11","Quantity":1,"Cost":"$1000","Selling":"$1050"},
{"Text":"Just got Adidas Nite Jogger 3M - Cloud White size 10 for $130 selling price is $180","Name":"Adidas Nite Jogger 3M - Cloud White","SKU":"none","Size":"10","Quantity":1,"Cost":"$130","Selling":"$180"},
{"Text":"Scored a Nike Air Max 1 Patta - Cherrywood in size 9 for $800 will be sold for $850","Name":"Nike Air Max 1 Patta - Cherrywood","SKU":"none","Size":"9","Quantity":1,"Cost":"$800","Selling":"$850"},
{"Text":"Just received 3 pairs of Adidas Yeezy Boost 350 V2 Black Non-Reflective SKU-234FSZ size 10 bought each for $220 aiming to sell each for $270","Name":"Yeezy Boost 350 V2 Black Non-Reflective","SKU":"234FSZ","Size":"10","Quantity":3,"Cost":"$220","Selling":"$270"},
{"Text":"Acquired 5 pairs of Air Jordan 4 Retro Bred 2019 SKU-2901SW size 9.5 cost per pair was $200 planning to sell each for $250","Name":"Jordan 4 Retro Bred 2019","SKU":"2901SW","Size":"9.5","Quantity":5,"Cost":"$200","Selling":"$250"},
{"Text":"Picked up 2 pairs of Nike Dunk Low University Blue SKU-879DSQ size 11 bought each for $185 reselling price is $235 each","Name":"Nike Dunk Low University Blue","SKU":"879DSQ","Size":"11","Quantity":2,"Cost":"$185","Selling":"$235"},
{"Text":"Managed to get 4 pairs of Yeezy Boost 700 Mauve SKU-091ZXV size 10.5 cost was $300 per pair will be sold for $350 each","Name":"Yeezy Boost 700 Mauve","SKU":"091ZXV","Size":"10.5","Quantity":4,"Cost":"$300","Selling":"$350"},
{"Text":"Scored 1 pair of New Balance 992 Joe Freshgoods - No Emotions are Emotions SKU-662LKM size 9 bought for $270 selling price is $320","Name":"New Balance 992 Joe Freshgoods","SKU":"662LKM","Size":"9","Quantity":1,"Cost":"$270","Selling":"$320"},
{"Text":"Purchased 2 pairs of Nike SB Dunk Low Ben & Jerry Chunky Dunky SKU-378GHS in size 12 cost per pair was $1000 hope to sell each for $1050","Name":"Nike SB Dunk Low Ben & Jerry Chunky Dunky","SKU":"378GHS","Size":"12","Quantity":2,"Cost":"$1000","Selling":"$1050"},
{"Text":"Just received 3 pairs of Air Jordan 1 Retro High Dark Mocha SKU-9076TF size 8.5 each cost me $210 looking to sell each for $260","Name":"Air Jordan 1 Retro High Dark Mocha","SKU":"9076TF","Size":"8.5","Quantity":3,"Cost":"$210","Selling":"$260"},
{"Text":"Acquired 1 pair of Yeezy 500 Utility Black SKU-256FRD size 11.5 which cost me $220 and I am selling it for $270","Name":"Yeezy 500 Utility Black","SKU":"256FRD","Size":"11.5","Quantity":1,"Cost":"$220","Selling":"$270"},
{"Text":"Got 4 pairs of Adidas NMD_R1 V2 MHA - My Hero Academia SKU-800BHU size 9 each for $180 will be sold for $230 each","Name":"Adidas NMD_R1 V2 MHA - My Hero Academia","SKU":"800BHU","Size":"9","Quantity":4,"Cost":"$180","Selling":"$230"},
{"Text":"Managed to buy 2 pairs of Nike Air Force 1 Low Off-White - Volt SKU-475BHT size 10.5 cost per pair was $300 selling them for $350 each","Name":"Nike Air Force 1 Low Off-White - Volt","SKU":"475BHT","Size":"10.5","Quantity":2,"Cost":"$300","Selling":"$350"},
{"Text":"Bought 2 pairs of Adidas Yeezy Boost 700 V2 Cream 256ZXC size 9.5 each for $300 selling each for $350","Name":"Adidas Yeezy Boost 700 V2 Cream","SKU":"124GHJ","Size":"9.5","Quantity":4,"Cost":"$300","Selling":"$350"},
{"Text":"Received 3 pairs of Air Jordan 5 Retro Raging Bull 2021 871FTG size 10 each costing $240 selling for $290 each","Name":"Air Jordan 5 Retro Raging Bull 2021","SKU":"300RTH","Size":"10","Quantity":5,"Cost":"$240","Selling":"$290"},
{"Text":"Acquired 5 pairs of Yeezy 700 V3 Kyanite 564RTY size 11 each costing $220 selling each for $270","Name":"Yeezy 700 V3 Kyanite","SKU":"503JKL","Size":"11","Quantity":2,"Cost":"$220","Selling":"$270"},
{"Text":"Picked up 1 pair of Jordan 1 Retro High Off-White University Blue 909ZXE size 8.5 for $1000 selling for $1050","Name":"Jordan 1 Retro High Off-White University Blue","SKU":"900JKL","Size":"8.5","Quantity":1,"Cost":"$1000","Selling":"$1050"},
{"Text":"Got 2 pairs of Air Jordan 3 Retro Cool Grey 2021 321RTZ size 10.5 each costing $200 selling for $250 each","Name":"Air Jordan 3 Retro Cool Grey 2021","SKU":"303RTY","Size":"10.5","Quantity":3,"Cost":"$200","Selling":"$250"},
{"Text":"Received 3 pairs of Nike SB Dunk Low Sean Cliver - Holiday Special 457EFG size 9 each for $220 reselling for $270 each","Name":"Nike SB Dunk Low Sean Cliver - Holiday Special","SKU":"113RTY","Size":"9","Quantity":4,"Cost":"$220","Selling":"$270"},
{"Text":"Scored 4 pairs of Air Jordan 6 Retro Carmine 2021 903GHD size 12 each for $230 selling each for $280","Name":"Air Jordan 6 Retro Carmine 2021","SKU":"301RTY","Size":"12","Quantity":5,"Cost":"$230","Selling":"$280"},
{"Text":"Purchased 5 pairs of Yeezy Boost 350 V2 Zyon 507JKL size 11.5 each for $200 reselling each for $250","Name":"Yeezy Boost 350 V2 Zyon","SKU":"504JKL","Size":"11.5","Quantity":1,"Cost":"$200","Selling":"$250"},
{"Text":"Acquired 2 pairs of Nike Air Force 1 Low Off-White - MCA Chicago 107DGF size 8 each for $1100 selling each for $1150","Name":"Nike Air Force 1 Low Off-White - MCA Chicago","SKU":"114RTY","Size":"8","Quantity":2,"Cost":"$1100","Selling":"$1150"},
{"Text":"Just received 3 pairs of Air Jordan 1 Retro High 85 Neutral Grey 901VFR size 10 each costing $240 selling for $290 each","Name":"Air Jordan 1 Retro High 85 Neutral Grey","SKU":"302RTY","Size":"10","Quantity":3,"Cost":"$240","Selling":"$290"},
{"Text":"Managed to get 4 pairs of Nike Air Max 97 Sean Wotherspoon 507JKU size 9.5 each for $230 selling each for $280","Name":"Nike Air Max 97 Sean Wotherspoon","SKU":"123RTY","Size":"9.5","Quantity":4,"Cost":"$230","Selling":"$280"},
{"Text":"Just received 5 pairs of Jordan 1 Retro High Obsidian UNC 908KJH size 11 each costing $210 reselling for $260 each","Name":"Jordan 1 Retro High Obsidian UNC","SKU":"902JKL","Size":"11","Quantity":5,"Cost":"$210","Selling":"$260"},
{"Text":"Got 1 pair of Nike LD Waffle Sacai Black Nylon 905TRF size 8.5 for $190 selling for $240","Name":"Nike LD Waffle Sacai Black Nylon","SKU":"115RTY","Size":"8.5","Quantity":1,"Cost":"$190","Selling":"$240"},
{"Text":"Purchased 2 pairs of Yeezy Boost 350 V2 Bred 506VGT size 10.5 each for $220 selling each for $270","Name":"Yeezy Boost 350 V2 Bred","SKU":"505JKL","Size":"10.5","Quantity":2,"Cost":"$220","Selling":"$270"},
{"Text":"Acquired 3 pairs of Jordan 1 Retro High Royal Toe 907DSE size 9 each costing $210 reselling each for $260","Name":"Jordan 1 Retro High Royal Toe","SKU":"901JKL","Size":"9","Quantity":3,"Cost":"$210","Selling":"$260"},
{"Text":"Received 4 pairs of Nike SB Dunk Low Strangelove 456GTH size 10 each for $220 reselling each for $270","Name":"Nike SB Dunk Low Strangelove","SKU":"112RTY","Size":"10","Quantity":4,"Cost":"$220","Selling":"$270"},
{"Text":"Bought 5 pairs of Jordan 1 Retro High Off-White White 902TRE size 8.5 each for $1050 selling each for $1100","Name":"Jordan 1 Retro High Off-White White","SKU":"115FRT","Size":"8.5","Quantity":5,"Cost":"$1050","Selling":"$1100"},
{"Text":"Scored 2 pairs of Yeezy Boost 350 V2 Israfil 509JKL size 12 each for $200 selling each for $250","Name":"Yeezy Boost 350 V2 Israfil","SKU":"506JKL","Size":"12","Quantity":1,"Cost":"$200","Selling":"$250"},
{"Text":"Picked up 3 pairs of Yeezy 500 Soft Vision 256ASD size 11.5 each for $220 reselling for $270 each","Name":"Yeezy 500 Soft Vision","SKU":"256ASD","Size":"11.5","Quantity":2,"Cost":"$220","Selling":"$270"},
{"Text":"Got 4 pairs of Nike Dunk Low SP Syracuse 2020 123FRT size 8 each for $200 selling each for $250","Name":"Nike Dunk Low SP Syracuse 2020","SKU":"123FRT","Size":"8","Quantity":4,"Cost":"$200","Selling":"$250"},
{"Text":"Managed to buy 5 pairs of Yeezy Boost 380 Alien 508JKL size 9 each for $240 selling for $290 each","Name":"Yeezy Boost 380 Alien","SKU":"508JKL","Size":"9","Quantity":5,"Cost":"$240","Selling":"$290"},
{"Text":"Just received 1 pair of Jordan 1 Retro High Pine Green Black Toe 905DES size 10 for $220 reselling for $270","Name":"Jordan 1 Retro High Pine Green Black Toe","SKU":"905DES","Size":"10","Quantity":1,"Cost":"$220","Selling":"$270"},
{"Text":"Acquired 2 pairs of Jordan 1 Retro High Court Purple White 906TRE size 9.5 each for $210 selling for $260 each","Name":"Jordan 1 Retro High Court Purple White","SKU":"906TRE","Size":"9.5","Quantity":2,"Cost":"$210","Selling":"$260"},
{"Text":"Bought 3 pairs of Yeezy Boost 350 V2 Tail Light 510VGT size 11 each for $200 selling each for $250","Name":"Yeezy Boost 350 V2 Tail Light","SKU":"510VGT","Size":"11","Quantity":3,"Cost":"$200","Selling":"$250"},
{"Text":"Received 4 pairs of Yeezy QNTM Teal Blue 512JKL size 8.5 each for $220 selling each for $270","Name":"Yeezy QNTM Teal Blue","SKU":"512JKL","Size":"8.5","Quantity":4,"Cost":"$220","Selling":"$270"},
{"Text":"Picked up 5 pairs of Air Jordan 4 Retro Fire Red 2020 322ERT size 10.5 each for $200 selling for $250 each","Name":"Air Jordan 4 Retro Fire Red 2020","SKU":"322ERT","Size":"10.5","Quantity":5,"Cost":"$200","Selling":"$250"},
{"Text":"Managed to get 1 pair of Yeezy Boost 350 V2 Lundmark Non-Reflective 511KJH size 9 for $220 selling for $270","Name":"Yeezy Boost 350 V2 Lundmark Non-Reflective","SKU":"511KJH","Size":"9","Quantity":1,"Cost":"$220","Selling":"$270"},
{"Text":"Scored 2 pairs of Nike Dunk Low Off-White - Pine Green 200TRE size 10 each for $1000 selling for $1050 each","Name":"Nike Dunk Low Off-White - Pine Green","SKU":"200TRE","Size":"10","Quantity":2,"Cost":"$1000","Selling":"$1050"},
{"Text":"Acquired 3 pairs of Yeezy 700 V3 Alvah 565YUH size 8.5 each for $220 reselling each for $270","Name":"Yeezy 700 V3 Alvah","SKU":"565YUH","Size":"8.5","Quantity":3,"Cost":"$220","Selling":"$270"},
{"Text":"Got 4 pairs of Jordan 1 Retro High Light Smoke Grey 903DES size 11 each for $210 selling each for $260","Name":"Jordan 1 Retro High Light Smoke Grey","SKU":"903DES","Size":"11","Quantity":4,"Cost":"$210","Selling":"$260"},
{"Text":"I want to add 2 pairs of Nike Air Max 1/97 VF Sean Wotherspoon in size 8.5 they cost around $300 each SKU: 257ZXW","Name":"Nike Air Max 1/97 VF Sean Wotherspoon","SKU":"257ZXW","Size":"8.5","Quantity":2,"Cost":"$300","Selling":"none"},
{"Text":"We're restocking 3 Jordan 1 Retro High Patina in size 9.5 with a cost of $230 each SKU: 125DES","Name":"Jordan 1 Retro High Patina","SKU":"125DES","Size":"9.5","Quantity":3,"Cost":"$230","Selling":"none"},
{"Text":"Yeezy Boost 700 Wave Runner in size 11 are being added We have 5 pairs at a cost of $270 each SKU: 777GHT","Name":"Yeezy Boost 700 Wave Runner","SKU":"777GHT","Size":"11","Quantity":5,"Cost":"$270","Selling":"none"},
{"Text":"I want to add 4 pairs of Jordan 1 Retro High Dark Mocha in size 9 they cost around $240 each SKU: 256LMN","Name":"Jordan 1 Retro High Dark Mocha","SKU":"256LMN","Size":"9","Quantity":4,"Cost":"$240","Selling":"none"},
{"Text":"Adding 3 pairs of Air Force 1 Low Travis Scott - Cactus Jack in size 10 at a cost of $320 each SKU: 123GHN","Name":"Air Force 1 Low Travis Scott - Cactus Jack","SKU":"123GHN","Size":"10","Quantity":3,"Cost":"$320","Selling":"none"},
{"Text":"5 pairs of Jordan 1 Retro High Shadow 2.0 in size 10.5 are being added with a cost of $230 each SKU: 444YUH","Name":"Jordan 1 Retro High Shadow 2.0","SKU":"444YUH","Size":"10.5","Quantity":5,"Cost":"$230","Selling":"none"},
{"Text":"I want to add 1 pair of Nike LD Waffle Sacai Pine Green in size 11 They cost around $290 each SKU: 352DES","Name":"Nike LD Waffle Sacai Pine Green","SKU":"352DES","Size":"11","Quantity":1,"Cost":"$290","Selling":"none"},
{"Text":"We're restocking 2 pairs of Air Jordan 1 Retro High OG University Blue in size 8.5 at a cost of $260 each SKU: 563FGH","Name":"Air Jordan 1 Retro High OG University Blue","SKU":"563FGH","Size":"8.5","Quantity":2,"Cost":"$260","Selling":"none"},
{"Text":"Yeezy Boost 350 V2 Static Reflective in size 9 are being added We have 4 pairs at a cost of $300 each SKU: 891ZXV","Name":"Yeezy Boost 350 V2 Static Reflective","SKU":"891ZXV","Size":"9","Quantity":4,"Cost":"$300","Selling":"none"},
{"Text":"I want to add 5 pairs of Jordan 1 Retro High Banned 2016 in size 9.5 they cost around $260 each SKU: 125VBN","Name":"Jordan 1 Retro High Banned 2016","SKU":"125VBN","Size":"9.5","Quantity":5,"Cost":"$260","Selling":"none"},
{"Text":"Adding 1 pair of Air Jordan 4 Retro Taupe Haze in size 11 at a cost of $240 each SKU: 678RTH","Name":"Air Jordan 4 Retro Taupe Haze","SKU":"678RTH","Size":"11","Quantity":1,"Cost":"$240","Selling":"none"},
{"Text":"2 pairs of Nike Dunk Low Ceramic 2020 in size 8.5 are being added with a cost of $230 each SKU: 956JKH","Name":"Nike Dunk Low Ceramic 2020","SKU":"956JKH","Size":"8.5","Quantity":2,"Cost":"$230","Selling":"none"},
{"Text":"I want to add 3 pairs of Yeezy Boost 350 V2 Yeshaya in size 10 They cost around $250 each SKU: 567RTY","Name":"Yeezy Boost 350 V2 Yeshaya","SKU":"567RTY","Size":"10","Quantity":3,"Cost":"$250","Selling":"none"},
{"Text":"We're restocking 4 pairs of Nike Dunk Low Retro Hyper Cobalt in size 9 at a cost of $200 each SKU: 345YUH","Name":"Nike Dunk Low Retro Hyper Cobalt","SKU":"345YUH","Size":"9","Quantity":4,"Cost":"$200","Selling":"none"},
{"Text":"Air Jordan 1 Mid Banned in size 10.5 are being added We have 5 pairs at a cost of $230 each SKU: 789VBN","Name":"Air Jordan 1 Mid Banned","SKU":"789VBN","Size":"10.5","Quantity":5,"Cost":"$230","Selling":"none"},
{"Text":"I want to add 1 pair of Nike Air Max 90 Bacon 2021 in size 11 They cost around $220 each SKU: 234YHN","Name":"Nike Air Max 90 Bacon 2021","SKU":"234YHN","Size":"11","Quantity":1,"Cost":"$220","Selling":"none"},
]

convert_json_to_jsonl(json_objects)
