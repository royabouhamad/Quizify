function limit_checkbox(name,obj,max)
   {
   var count=1;

   var x=document.getElementsByName(name);
   for (var i=0; i < x.length; i++)
      {
      if(x[i].checked)

       {
         count = count + 1;
     }
    }
   if (count > max)
    {
    alert('Please select only 1 checkbox.');
    obj.checked = false;
      }
    }
