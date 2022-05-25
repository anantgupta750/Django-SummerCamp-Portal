function main()
{
    var status=true
    id=document.getElementById("txtid").value
    pasword=document.getElementById("txtpass").value
    cname=document.getElementById("txtcname").value
    oname=document.getElementById("txtoname").value
    email=document.getElementById("txtemail").value
    campnumber=document.getElementById("txtphonenumber").value
    address=document.getElementById("txtaddress").value
    des=document.getElementById("txtdes").value
  
    if(id.length==0)
    {
        document.getElementById("idmsg").innerText="*SummerCamp ID Required"
        status=false
    }
    if(password.length==0)
    {
        document.getElementById("passmsg").innerText="*Password Required"
        status=false
    }
    if(cname.length==0)
    {
        document.getElementById("campnamemsg").innerText="*Camp Name Required"
        status=false
    }
    if(oname.length==0)
    {
        document.getElementById("ownernamemsg").innerText="*Owner Name Required"
        status=false
    }
    if(email.length==0)
    {
        document.getElementById("emailmsg").innerText="*Camp Email Required"
        status=false
    }
    if(campnumber.length==0)
    {
        document.getElementById("phonemsg").innerText="*PhoneNumber Required"
        status=false
    }
    if(address.length==0)
    {
        document.getElementById("addressmsg").innerText="*Address Required"
        status=false
    }
    if(des.length==0)
    {
        document.getElementById("desmsg").innerText="*Description Required"
        status=false
    }
   
    return status
}