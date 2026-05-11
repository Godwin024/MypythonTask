def get_temp_advisory_control(temperature, temp_threshold, unit = "C"):
    if unit.upper() == "C":
        temperature = (temperature * 9/5) + 32
        temp_threshold = (temp_threshold * 9/5) + 32
    elif unit.upper() == "F":
        temperature = (temperature - 32)*5/9
        temp_threshold = (temp_threshold - 32)*5/9
    else:
        raise ValueError("Invalid unit!")
    if temperature < temp_threshold:
        return temperature, "cold advisory"
    elif  temperature >= temp_threshold:
        return temperature, "Heat alert"
    
    
        
        
     
    
        
        
    
     










