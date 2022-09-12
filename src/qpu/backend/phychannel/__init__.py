from qpu.backend.phychannel.physical_channel import PhysicalChannel, UpConversionChannel, DACChannel


def from_dict( channel:dict )->PhysicalChannel:
    category = channel["type"]
    name = channel["id"]
    #print("api", name, category)
    devices = channel["devices"]
    match category:
        case "upconversion":    
            PChObj = UpConversionChannel(name)
            PChObj.devices = devices
        case "dir_output":    
            PChObj = DACChannel(name)
            PChObj.devices = devices
        case _:
            print("channel category not defined")
            return None
    PChObj.port = channel["port"]

    print(f"api name: {PChObj.name} port:{PChObj.port} class: {type(PChObj)}")

    return PChObj

    
