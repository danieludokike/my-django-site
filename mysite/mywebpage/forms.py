from django import forms


class ContactMeForm(forms.Form):
	full_name = forms.CharField(
		max_length=200,
		widget=forms.TextInput(
			attrs={
				'placeholder': 'FULL NAME',
				'class': 'full_name_input',
			}
		)
	)

	email = forms.CharField(
		max_length=200,
		widget=forms.EmailInput(
			attrs={
				'placeholder': 'EMAIL ADDRESS',
				'class': 'email_input',
			}
		)
	)

	subject = forms.CharField(
		max_length=200,
		widget=forms.TextInput(
			attrs={
				'placeholder': 'ENTER SUBJECT',
				'class': 'subject_input',
			}
		)
	)

	text = forms.CharField(
		required=True,
		widget=forms.Textarea(
			attrs={
				'placeholder': 'Leave Us a Message Here!!',
				'class': 'text_input',
			}
		)
	)
