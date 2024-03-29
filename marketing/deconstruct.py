from datetime import datetime
from .jsons import *



class Deconstruct:
    def __init__(self,data):
        self.data=data
     
        
    def consign_address(self):
        
        consign=dict()
        for i in consign_add_key:
            consign.update({i:self.data[i]})
   
        consign.update({"type":"consign"})
        consign.update({"group":self.data["woso_no"]})
    
        consign['org']=consign.pop('consignee_org')
        consign['address_line_1']=consign.pop('consignee_addr_line1')
        consign['address_line_2']=consign.pop('consignee_addr_line2')
        consign['address_line_3']=consign.pop('consignee_addr_line3')
        consign['pin']=consign.pop('consignee_pin')
        consign['phone_no']=consign.pop('consignee_phone_no')
        consign['gst_no']=consign.pop('consignee_gst_no')
        
        
        
        return consign
 
    def buyer_addr(self):
        buyer=dict()
        
        
        for i in buyer_keys:
            buyer.update({i:self.data[i]})
   
        buyer.update({"type":"buyer"})
        buyer.update({"group":self.data["woso_no"]})
        buyer['org']=buyer.pop('buyer_org')
        buyer['address_line_1']=buyer.pop('buyer_addr_line1')
        buyer['address_line_2']=buyer.pop('buyer_addr_line2')
        buyer['address_line_3']=buyer.pop('buyer_addr_line3')
        buyer['pin']=buyer.pop('buyer_pin')
        buyer['phone_no']=buyer.pop('buyer_phone_no')
        buyer['gst_no']=buyer.pop('buyer_gst_no')
  
  
        return buyer
    
    def marketing(self):
        mkt=dict()
       
        
        for i in mkt_keys:
            mkt.update({i:self.data[i]})
        
       
        mkt['no']=mkt.pop('woso_no')
        mkt['date']=mkt.pop('woso_date')
        mkt['marketing_item']=mkt.pop('item')
        
        return mkt
    
        
    
    def item_deconstruct(self):
        items=list()
        item=list()
        items=self.data["items"]
        
        for i in items:
            d=dict(i)
            d.update({'item_group':self.data['woso_no']})
            item.append(d)
    
            
      
        return item
  
        