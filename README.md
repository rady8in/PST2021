# PST2021
Fool Me Once: A Study of Password Selection Evolution over the Past Decade<hr>

**Algorithm 1**<br>
Simplified algorithm for finding date and service related to leaked credentials using the API<br><br>
**Input:** The email address to check and a list of header variables including the API key <br>
**Output:** A list containing information about matching breaches where the provided email address was found<br><br>
<i>response</i> &leftarrow; HTTP_GET(<i>URL, email, header</i>)<br>
<b>return</b> <i>response</i>[<i>name, breach_date</i>]
<br><br>
For code example, check API_Usage.py
<hr>

<b>Algorithm 2</b> <br>
Simplified algorithm for filtering credentials on our requirements<br><br>
<i>invalid_list</i> &leftarrow; [hashes with count>=cutoff]<br>
<b>while</b> ! EOF credential_list <b>do</b><br>
&nbsp;&nbsp;_values_ &leftarrow; next set of credentials<br>
&nbsp;&nbsp;_values_.drop_duplicate_emails()<br>
&nbsp;&nbsp;_values_.drop_invalid_emails()<br>
&nbsp;&nbsp;**for all** _item_ in _values_ **do**<br>
&nbsp;&nbsp;&nbsp;&nbsp;**if** _item_['pass'].hash() in _invalid_list_ **then**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_values_.drop(_item_)<br>
&nbsp;&nbsp;&nbsp;&nbsp;**end if**<br>
&nbsp;&nbsp;**end for**<br>
&nbsp;&nbsp;output &leftarrow; values<br>
**end while**<br>
<hr>


**Algorithm 3**<br>
Simplified algorithm for marking credentials that are part of exactly one leak<br><br>
_processed_ = []<br>
_unprocessed_ = []<br>
**procedure** LOADDATA<br>
&nbsp;&nbsp;**while** ! EOF credential_list **do**<br>
&nbsp;&nbsp;&nbsp;&nbsp;_unprocessed_.append(next set of credentials)<br>
&nbsp;&nbsp;**end while<br>
end procedure<br>
procedure** APICHECK<br>
&nbsp;&nbsp;**for all** _item_ in _unprocessed_ **do**<br>
&nbsp;&nbsp;&nbsp;&nbsp;_APIResponse_ = Call_API(_item_)<br>
&nbsp;&nbsp;&nbsp;&nbsp;**if** _APIResponse_.status_code == 200 **then**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_value_ = _item_.extend(_APIResponse_.json())<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_processed_.append(_value_)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_unprocessed_.delete(_item_)<br>
&nbsp;&nbsp;&nbsp;&nbsp;**else**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Raise Error<br>
&nbsp;&nbsp;&nbsp;&nbsp;**end if**<br>
&nbsp;&nbsp;&nbsp;&nbsp;Sleep(1.5)<br>
&nbsp;&nbsp;**end for<br>
end procedure<br>
procedure** EXPORTVALID<br>
&nbsp;&nbsp;**for all** _item_ in _processed_ **do<br>
&nbsp;&nbsp;&nbsp;&nbsp;if** len(_item_) == 1 **then**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output &leftarrow; _item_.requiredFields<br>
&nbsp;&nbsp;&nbsp;&nbsp;**end if**<br>
&nbsp;&nbsp;&nbsp;&nbsp;_processed_.delete(_item_)<br>
&nbsp;&nbsp;**end for<br>
end procedure<br>
Ensure:** The procedures are run as parallel threads<br>
<hr>
