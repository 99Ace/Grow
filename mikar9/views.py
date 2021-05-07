from django.shortcuts import render, HttpResponse, redirect
from .forms import NewInvoice
from .models import Invoice
from log.models import LogRecord
import datetime

# Create your views here.


def mikar9(request):
    return render(request, 'index.html')


def add(request):
    if request.method == "POST":
        new_entry = NewInvoice(request.POST)
        if new_entry.is_valid():
            # Get the input from form
            instance = new_entry.save(commit=False)

            # Extract date information
            inv_date = request.POST.get('inv_date')
            new_entry.inv_date = datetime.datetime.strptime(
                inv_date, '%Y-%m-%d'
            )
            instance.inv_date = inv_date
            # FINANCIAL_YEAR
            print(
                new_entry.inv_date.year,
                new_entry.inv_date.month,
                new_entry.inv_date.day
            )
            instance.financial_year = new_entry.inv_date.year
            # MONTH
            instance.month = new_entry.inv_date.month

            # USERNAME
            instance.submitter = request.user

            # store log data
            instance.save()
            print('New Entry Saved')

            log_details = "{} of ${} is submitted by {}".format(
                instance.invoice,
                instance.inv_date,
                instance.submitter,

            )
            newlog = LogRecord(
                invoice=instance.invoice,
                action="Create new expense",
                changes=log_details,
                submitter=instance.submitter
            )
            newlog.save()
            print("Log is saved")

            return redirect(mikar9)

    form = NewInvoice()
    return render(request, 'add.html', {
        'form': form
    })


def show(request):
    data = Invoice.objects.all()
    return render(request, 'show.html', {
        'data': data
    })
