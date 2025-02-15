
export const formatNumber = function(value) {
  if (value && parseFloat(value)){
    let parts = parseFloat(value).toFixed(2).toString().split(".");

    parts[0]=(parts[0]).replace(/\d(?=(\d{3})+$)/g, "$&\xa0")
    if (parts.length==1){
          parts.push('00')
    }
    return parts.join(',')
  }else{
    if (value === null){
        return 0 
    }else if(value=== undefined){
        return ''
    }else{
        return value
    }

  }
} 

