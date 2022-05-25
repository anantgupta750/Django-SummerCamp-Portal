function main()
{
    var status=true
    oname=document.getElementById("txtname").value
    email=document.getElementById("txtemail").value
    cname=document.getElementById("txtcampname").value
    rating=document.getElementById("cmbrating").value
    feedback=document.getElementById("txtfeedback").value
    
    if(oname.length==0)
    {
        document.getElementById("namemsg").innerHTML="*Name Required"
        status=false
    }
    if(email.length==0)
    {
        document.getElementById("emailmsg").innerText="*Email Required"
        status=false
    }
    if(cname.length==0)
    {
        document.getElementById("campnamemsg").innerHTML="*Camp Name Required"
        status=false
    }
    if(feedback.length==0)
    {
        document.getElementById("feedbackmsg").innerText="*Feedback Required"
        status=false
    }
    if(rating=="default")
    {
        document.getElementById("ratingmsg").innerText="*Rating Required"
        status=false
    }
    return status
}