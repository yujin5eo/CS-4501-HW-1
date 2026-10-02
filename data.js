window.BLOOM_DATA = {
  product: { id:'bumblebee', name:'Bumblebee flowers', unitCents:2500 },
  products:[
    ['thimble-star','Thimble Star',2200],['moon-mallow','Moon Mallow',2600],['bumblebee','Bumblebee flowers',2500],
    ['violet-whistle','Violet Whistle',2400],['clover-crown','Clover Crown',2100],['garden-comet','Garden Comet',2800]
  ].map(([id,name,unitCents])=>({id,name,unitCents})),
  wraps:[['WG04','Moss Picnic Paper'],['WG17','Ivory Garden Wrap'],['BK22','Bluebell Kraft'],['HV09','Honey-Violet Sleeve']].map(([code,name])=>({code,name})),
  deliveries:[
    ['Dusk Drifter','16:00–18:00',1200],['Orchard Relay','11:00–13:00',1800],['Morning Flight','09:00–11:00',2400],['Clover Express','08:00–10:30',2900],['Petal Post','13:00–16:00',900],['Hive Priority','10:00–12:00',2100],['Sunrise Wing','07:00–09:00',1900],['Meadow Loop','14:00–17:00',1500],['Royal Courier','09:30–11:30',2300],['Garden Gallop','12:00–14:00',1700],['Pollen Parcel','15:00–18:00',1100],['Nectar Now','08:30–10:30',2800],['Bluebell Route','10:30–12:30',1600],['Willow Wagon','09:00–12:00',1300],['Honey Haul','17:00–19:00',1000],['Dewdrop Dispatch','06:00–08:00',1400],['Briar Byway','11:30–14:30',800],['Queen’s Reserve','09:00–11:00',3100]
  ].map(([name,window,cents],i)=>({id:'d'+i,name,window,cents})),
  promo:'741906283517', constraints:{quantity:12,wrap:'WG17',delivery:'Morning Flight',date:'2026-10-24',recipient:'Turnipseed Wedding',venue:'Meadow Hall',email:'planner@example.com',maxCents:29500}
};
window.money = cents => '$'+(cents/100).toFixed(2);
