from inventory import Inventory
from instrument_spec import InstrumentSpec
from instrument_type import InstrumentType
from instrument import Instrument
from builder import Builder
from wood import Wood
from type_ import Type




def inventory_init(inventory):
    
    instruments = list()
    
    #instrument full spec for Banjo #1
    
    instruments.append(['121829', 2500.55, InstrumentSpec({
            'instrument_type': InstrumentType.BANJO,
            'model': 'iknownothingofbanjo',
            'builder': Builder.FENDER,
            'wood': Wood.MAHOGANY,
            'numString': 8
    })])
 
    #instrument full spec for Banjo #2

    instruments.append(['230203', 1399.99, InstrumentSpec({
            'instrument_type': InstrumentType.BANJO,
            'model': 'iknownothingofbanjostill',
            'builder': Builder.FENDER,
            'wood': Wood.CEDAR,
            'numString': 16
    })])
    
    
    # Banjo #3
    
    properties = dict()
    
    properties['instrument_type'] = InstrumentType.BANJO
    properties['model'] = 'iknBanjo'
    properties['builder'] = Builder.MARTIN
    properties['wood'] = Wood.INDIAN_ROSEWOOD
    
    
    instruments.append(['118493', 4939.00, InstrumentSpec(properties)])

    #add instrument to inventory
    for instrument in instruments:
        inventory.add_instrument(instrument[0], instrument[1], instrument[2])
    
    
    #Guitar #1 - add to inventory
    inventory.add_instrument("349242", 9039.99, InstrumentSpec({
        'builder': Builder.FENDER,
        'model': "model", 
        'wood': Wood.CEDAR,
        'instrument_type': InstrumentType.GUITAR
    }))
    
    #Guitar #2
    inventory.add_instrument("349242", 9039.99, InstrumentSpec({
        'builder': Builder.OLSON,
        'model': "model#2", 
        'wood': Wood.MAHOGANY,
        'instrument_type': InstrumentType.GUITAR
    }))
    
    del properties
    return


inventory = Inventory()
inventory_init(inventory)


print(inventory.get_instrument_by_serial_num('230203'))
print()
search_spec = InstrumentSpec({'builder': Builder.FENDER, 'wood': Wood.MAHOGANY})

matching_instruments = inventory.search(search_spec)

if matching_instruments:
    for instrument in matching_instruments:
        spec = instrument.get_spec()
        instrument_type = spec.get_property("instrument_type").value
        print(f'We have a {instrument_type} (serial number: {instrument.get_serial_num()}) with the following properties: ')
        
        #surely a better way to unpack exists
        print(spec.get_properties())
        print(f'You can have this {instrument_type} for NGN{instrument.get_price()}')
else:
    print("No match found.")





    