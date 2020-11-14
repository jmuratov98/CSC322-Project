// Show div html based on role
if (HelpCenter.user.role=="user_surfer"){
 $("div.user_surfer").show();
}

if (HelpCenter.user.role=="user_member"){
 $("div.user_member").show();
}

if (HelpCenter.user.role=="chef"){
 $("div.chef").show();
}

if (HelpCenter.user.role=="manager"){
 $("div.manager").show();
}
