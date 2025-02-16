export const plantUrl= '/api/plantapp/plant/'
export const genusUrl= '/api/plantapp/genus/'
export const categoryUrl= '/api/plantapp/category/'
export const offerUrl= '/api/docapp/offer/'
export const offeritemUrl= '/api/docapp/offeritem/'
export const goodsUrl= '/api/stockapp/goods/'
export const counterpartyUrl= '/api/docapp/counterparty/'
export const userUrl= '/api/getUser/'


// import moment from 'moment'
// moment.locale('ru-ru')
import axios from 'axios'

export default   function toURLParams(filters){
    let params = new URLSearchParams();
    for (let f in filters){
        if (Array.isArray(filters[f])){
            for (let p of filters[f]){
                if (p){
                    params.append(f,p);
                }
            }
        }else if (filters[f] && filters[f].id){
            params.append(f,filters[f]['id'])

        }else{
                if (filters[f] !=undefined){
            params.append(f,filters[f]);
                }

        }
    }
    return params
}



async function _save(url,obj){
    let response 
    if (obj.id){
         response = await axios.patch(url+obj.id+'/',obj)
    }else{
         response = await axios.post(url,obj)
    }
    return response.data
}
    /*
async function _delete(url,obj){
    let response 
    if (obj.id){
         response = await axios.delete(url+obj.id+'/',obj)
    }
    
    return response
}
    */

async function _getList(url,filter){
    const response = await axios.get(url+'?'+toURLParams(filter))
    return response.data
}

async function _getById(url,id){
    const response = await axios.get(url+id+'/')
    return response.data
}



function apiConstructor(apiUrl){
    return {
        async save(obj){
            return _save(apiUrl,obj)
        },
        async get(obj){
            return _getById(apiUrl,obj)
        },
        async filter(filter){
            return _getList(apiUrl,filter)
        },
    }
}

export let Plant = {
    url:plantUrl,
    objects:apiConstructor(plantUrl)
}
export let Genus = {
    url:genusUrl,
    objects:apiConstructor(genusUrl)
}

export let Category = {
    url:categoryUrl,
    objects:apiConstructor(categoryUrl)
}


export let Offer = {
    url:offerUrl,
    objects:apiConstructor(offerUrl)
}

export let OfferItem = {
    url:offeritemUrl,
    objects:apiConstructor(offeritemUrl)
}

export let Goods = {
    url:goodsUrl,
    objects:apiConstructor(goodsUrl)
}

export let Counterparty = {
    url:counterpartyUrl,
    objects:apiConstructor(counterpartyUrl)
}

export  async function getUser(){
    return (await axios.get(userUrl)).data
}
