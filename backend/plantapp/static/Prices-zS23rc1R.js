import{H as f}from"./Header-B9Y5y78S.js";import{c as a,o as r,b as i,_ as u,m as _,a as p,p as l,t as h,C as v,y as k,s as g,u as w,z as y,l as b,F as d,i as x,x as C,h as P}from"./index-BWMkSv2y.js";import{a as S}from"./index-DW_MHI2K.js";const B={xmlns:"http://www.w3.org/2000/svg",width:"800",height:"800",fill:"none",viewBox:"0 0 24 24"};function N(t,e){return r(),a("svg",B,e[0]||(e[0]=[i("path",{stroke:"tomato","stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"1.5",d:"M12 7v7m0 0 3-3m-3 3-3-3"},null,-1),i("path",{stroke:"tomato","stroke-linecap":"round","stroke-width":"1.5",d:"M16 17H8M22 12c0 4.714 0 7.071-1.465 8.535C19.072 22 16.714 22 12 22s-7.071 0-8.536-1.465C2 19.072 2 16.714 2 12s0-7.071 1.464-8.536C4.93 2 7.286 2 12 2s7.071 0 8.535 1.464c.974.974 1.3 2.343 1.41 4.536"},null,-1)]))}const F={render:N},A={key:0,class:"file"},D={class:"file__name"},H={__name:"File",props:{filePath:{type:String,required:!0},fileName:{type:String,required:!0},isActive:{type:Boolean,required:!0}},setup(t){const e=t,s=()=>{const o=document.createElement("a");o.href=e.filePath,o.setAttribute=document.createAttribute("download",e.fileName),document.body.appendChild(o),o.click(),document.body.removeChild(o)};return(o,n)=>t.isActive?(r(),a("div",A,[p(l(F),{class:"file__svg"}),i("p",D,h(t.fileName),1),i("button",{onClick:s,class:"file__btn btn"},"Скачать")])):_("",!0)}},M=u(H,[["__scopeId","data-v-cbbd096c"]]),$=v("priceStore",()=>{const t=k();return{prices:t,getPrices:async()=>{try{const{data:s}=await S.get("/api/stockapp/price-files/");t.value=s.results}catch(s){console.error(s)}}}}),q={class:"prices"},V={class:"prices__box"},E={key:0,class:"prices__files"},I={__name:"Prices",setup(t){const e=$(),{prices:s}=g(e);return w({title:'Питомник "Красная Гвоздика"',meta:[{name:"description",content:'питомник растений "Красная Гвоздика"'},{name:"keywords",content:"цветы, растения, саженцы, кустарники, деревья, купить саженцы, купить растения"}]}),y(()=>{e.getPrices()}),(o,n)=>{const m=C("auto-animate");return r(),a(d,null,[p(f),i("section",q,[b((r(),a("div",V,[n[0]||(n[0]=i("h3",{class:"prices__title title"},"Прайс-лист",-1)),n[1]||(n[1]=i("p",{class:"prices__text"}," Внимание! Уважаемые клиенты! В текущей ситуации цены, указанные на сайте, не являются официальной офертой: цены могут меняться в зависимости от ситуации на рынке. Чтобы выяснить актуальные цены, обращайтесь к специалистам питомника. ",-1)),l(s)?(r(),a("div",E,[(r(!0),a(d,null,x(l(s),c=>(r(),P(M,{key:c.id,"file-path":c.file,"file-name":c.name,"is-active":c.is_active},null,8,["file-path","file-name","is-active"]))),128))])):_("",!0)])),[[m]])])],64)}}},R=u(I,[["__scopeId","data-v-de43990e"]]);export{R as default};
