from collections import defaultdict


@login_required
def resolved_tickets_by_club(request):
    # Retrieve all resolved tickets (where resolved_at is not null)
    resolved_tickets = Ticket.objects.filter(user=request.user, resolved_at__isnull=False)

    # Group tickets by club
    tickets_by_club = defaultdict(list)
    for ticket in resolved_tickets:
        if ticket.club:
            tickets_by_club[ticket.club] += [ticket]
        else:
            tickets_by_club["Unassigned"] += [ticket]

    context = {
        'tickets_by_club': tickets_by_club,
    }
    return render(request, 'FanSupport/resolved_tickets_by_club.html', context)
