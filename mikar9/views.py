from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import NewInvoice, EditInvoice
from .models import Invoice
from log.models import LogRecord
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.


def mikar9(request):
    # CODE TO SEND EMAIL
    send_mail(
        'Subject here',
        'Here is the message.',
        'chunliang.ang@gmail.com',
        ['chunliang.ang@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'index.html')


@login_required
def add(request):
    if request.method == "POST":
        new_entry = NewInvoice(request.POST)
        if new_entry.is_valid():
            # Get the input from form
            instance = new_entry.save(commit=False)

            # Extract date information
            inv_date = request.POST.get('inv_date')
            new_entry.inv_date = datetime.strptime(
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

            # SET THE CURRENT TIME
            now = datetime.now() + timedelta(hours=8)
            instance.log_datetime = now
            # store log data
            instance.save()
            print('New Entry Saved')

            log_details = "{} of ${} is submitted by {}".format(
                instance.invoice,
                instance.accounts_receivables,
                instance.submitter,

            )
            print(now)
            newlog = LogRecord(
                invoice=instance.invoice,
                action="CREATE",
                changes=log_details,
                submitter=instance.submitter,
                log_datetime=now
            )
            newlog.save()
            print("Log is saved")

            return redirect(mikar9)

    form = NewInvoice()
    return render(request, 'add.html', {
        'form': form
    })


@login_required
def edit(request, item_id):
    item = get_object_or_404(Invoice, pk=item_id)

    if request.method == "POST":
        new_entry = EditInvoice(request.POST, instance=item)
        if new_entry.is_valid():
            # Get the input from form
            instance = new_entry.save(commit=False)

            # Extract date information
            inv_date = request.POST.get('inv_date')
            new_entry.inv_date = datetime.strptime(
                inv_date, '%Y-%m-%d'
            )
            instance.inv_date = inv_date
            # FINANCIAL_YEAR
            instance.financial_year = new_entry.inv_date.year
            # MONTH
            instance.month = new_entry.inv_date.month

            # USERNAME
            instance.submitter = str(request.user)

            # SET THE CURRENT TIME
            now = datetime.now() + timedelta(hours=8)
            instance.log_datetime = now

            # reload in the picture
            instance.cover = item.cover

            instance.save()

            print('New Entry Saved')

            # store log data
            log_details = "{} of ${} is edited by {}".format(
                instance.invoice,
                instance.accounts_receivables,
                instance.submitter,
            )

            newlog = LogRecord(
                invoice=instance.invoice,
                action="EDIT",
                changes=log_details,
                submitter=instance.submitter,
                log_datetime=now
            )
            newlog.save()
            print("Log is saved")

            return redirect(mikar9)

    form = EditInvoice(instance=item)
    return render(request, 'edit.html', {
        'form': form
    })


@login_required
def show(request):
    data = Invoice.objects.all()
    return render(request, 'show.html', {
        'data': data
    })


@login_required
def delete(request, item_id):
    # retrieve item details
    item = get_object_or_404(Invoice, pk=item_id)

    # delete from database
    Invoice.objects.filter(pk=item_id).delete()

    # store log data
    # get current datetime
    now = datetime.now() + timedelta(hours=8)

    # create log details
    log_details = "{} of ${} is removed by {}".format(
        item.invoice,
        item.accounts_receivables,
        item.submitter,
    )

    newlog = LogRecord(
        invoice=item.invoice,
        action="DELETE",
        changes=log_details,
        submitter=request.user,
        log_datetime=now
    )
    newlog.save()
    print("Log is saved")

    return redirect(mikar9)


@login_required
def view_account(request, fy_selected, choice):
    data = []
    if request.method == "POST":
        if request.POST.get('financial_year') == "all":
            data = Invoice.objects.all().order_by('inv_date')
        else:
            fy_selected = int(request.POST.get('financial_year'))
            data = Invoice.objects.filter(financial_year=fy_selected).order_by('inv_date')
    else:
        if choice == "up":
            if fy_selected == "all":
                data = Invoice.objects.all().order_by('inv_date')
            else:
                data = Invoice.objects.filter(financial_year=fy_selected).order_by('inv_date')
        else:
            if fy_selected == "all":
                data = Invoice.objects.all().order_by('inv_date').reverse()
            else:
                data = Invoice.objects.filter(financial_year=fy_selected).order_by('inv_date').reverse()
            
    return render(request, 'view_account.html', {
        'data': data,
        'financial_year': fy_selected
    })


