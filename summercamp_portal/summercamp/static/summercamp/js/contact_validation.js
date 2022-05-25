function main()
{
    var status=true
    username=document.getElementById("txtname").value
    useremail=document.getElementById("txtemail").value
    userphone=document.getElementById("txtphonenumber").value
    userquestion=document.getElementById("txtques").value
    if(username.length==0)
    {
        document.getElementById("namemsg").innerHTML="*Name Required"
        status=false
    }
    if(useremail.length==0)
    {
        document.getElementById("emailmsg").innerText="*Email Required"
        status=false
    }
    if(userphone.length==0)
    {
        document.getElementById("phonemsg").innerText="*No. Required"
        status=false
    }
    if(userquestion.length==0)
    {
        document.getElementById("quesmsg").innerText="*Question Required"
        status=false
    }
    return status
}