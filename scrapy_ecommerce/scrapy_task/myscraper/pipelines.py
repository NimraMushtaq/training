from itemadapter import ItemAdapter


class LaptopPipeline:
    def process_item(self, item, spider):
        if spider.name == 'laptop_spider':
            adapter = ItemAdapter(item)

            if 'generation' in adapter:
                adapter['generation'] = adapter['generation'].replace('Generation', '').strip()

            if 'name' in adapter:
                name = adapter['name']
                if 'Apple' in name:
                    first_apple_index = name.index('Apple')
                    second_apple_index = name.find('Apple', first_apple_index + 1)

                    if second_apple_index != -1:
                        adapter['name'] = name[:second_apple_index].replace('\"', '').strip()
                        adapter['name'] = adapter['name'].replace('-', '').strip()
                else:
                    name_parts = name.rsplit(' - ', 1)
                    adapter['name'] = name_parts[0].replace('\"', '').strip()

            if 'screen_size' in adapter:
                screen_size = adapter['screen_size']
                words = screen_size.split()
                if '\"' in words[0]:
                    adapter['screen_size'] = words[0].replace('\"', '-inch')
                elif '"' in words[0]:
                    adapter['screen_size'] = words[0].replace('"', '-inch')
                elif 'inch' in words[0]:
                    inch_index = screen_size.find('inch')
                    content_till_inch = screen_size[:inch_index+4].strip()
                    adapter['screen_size'] = content_till_inch.replace('\"', '-inch')
                else:
                    opening_bracket_index = screen_size.find('(')
                    closing_bracket_index = screen_size.find(')')

                    if opening_bracket_index != -1 and closing_bracket_index != -1:
                        content_within_brackets = screen_size[opening_bracket_index + 1:closing_bracket_index].strip()
                        adapter['screen_size'] = content_within_brackets.replace('\"', '-inch')

            if 'price' in adapter:
                adapter['price'] = float(adapter['price'].replace('Rs. ', '').replace(',', ''))

            if 'weight' in adapter:
                adapter['weight'] = adapter['weight'].lower()
                adapter['weight'] = adapter['weight'].replace('starting at', '').strip()
                adapter['weight'] = adapter['weight'].replace('around', '').strip()
                adapter['weight'] = adapter['weight'].replace('lb', 'pounds').strip()
                weight_words = adapter['weight'].split()
                adapter['weight'] = ' '.join(weight_words[:2])

                if 'pounds' in adapter['weight']:
                    pounds_index = adapter['weight'].index('pounds')
                    weight_in_pounds = float(adapter['weight'][:pounds_index].strip())
                    weight_in_kg = weight_in_pounds * 0.453592
                    adapter['weight'] = f"{weight_in_kg:.2f} kg"

            if 'color' in adapter:
                adapter['color'] = adapter['color'].strip().lower()

            if 'screen_resolution' in adapter:
                if adapter['screen_resolution'] is None:
                    adapter['screen_resolution'] = 'null'
                else:
                    adapter['screen_resolution'] = adapter['screen_resolution'].strip()
            if 'ssd' in adapter:
                adapter['ssd'] = adapter['ssd'].strip()
            if 'installed_ram' in adapter:
                adapter['installed_ram'] = adapter['installed_ram'].strip()
            if 'brand' in adapter:
                adapter['brand'] = adapter['brand'].strip().lower()

            return item


class AirpodPipeline:
    def process_item(self, item, spider):
        if spider.name == 'airpod_spider':
            adapter = ItemAdapter(item)
            if 'name' in adapter:
                name = adapter['name']
                name_parts = name.rsplit(' - ', 1)
                adapter['name'] = name_parts[0].replace('\"', '').strip()
            if 'color' in adapter:
                name = adapter['name']
                if 'UNIQ' in name:
                    hyphen_index = name.find('–')
                    color_part = name[hyphen_index + 1:].strip().lower()
                    adapter['color'] = color_part
                else:
                    adapter['color'] = adapter['color'].strip().lower()
            if 'brand' in adapter:
                name = adapter['name'].split(' ')
                adapter['brand'] = name[0]
            if 'price' in adapter:
                adapter['price'] = float(adapter['price'].replace('Rs. ', '').replace(',', ''))

            return item
