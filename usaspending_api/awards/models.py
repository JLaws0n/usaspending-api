from django.db import models
from django.db.models import F, Q, Sum

from usaspending_api.accounts.models import AppropriationAccountBalances
from usaspending_api.submissions.models import SubmissionAttributes
from usaspending_api.references.models import RefProgramActivity, RefObjectClassCode, Agency, Location, LegalEntity
from usaspending_api.common.models import DataSourceTrackedModel


class FinancialAccountsByAwards(DataSourceTrackedModel):
    financial_accounts_by_awards_id = models.AutoField(primary_key=True)
    appropriation_account_balances = models.ForeignKey(AppropriationAccountBalances, models.CASCADE)
    submission = models.ForeignKey(SubmissionAttributes, models.CASCADE)
    award = models.ForeignKey('awards.Award', models.CASCADE, null=True, related_name="financial_set")
    program_activity_name = models.CharField(max_length=164, blank=True, null=True)
    program_activity_code = models.ForeignKey(RefProgramActivity, models.DO_NOTHING, db_column='program_activity_code', blank=True, null=True)
    object_class = models.ForeignKey(RefObjectClassCode, models.DO_NOTHING, null=True, db_column='object_class')
    by_direct_reimbursable_funding_source = models.CharField(max_length=1, blank=True, null=True)
    piid = models.CharField(max_length=50, blank=True, null=True)
    parent_award_id = models.CharField(max_length=50, blank=True, null=True)
    fain = models.CharField(max_length=30, blank=True, null=True)
    uri = models.CharField(max_length=70, blank=True, null=True)
    award_type = models.CharField(max_length=30, blank=True, null=True)
    ussgl480100_undelivered_orders_obligations_unpaid_fyb = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl480100_undelivered_orders_obligations_unpaid_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl483100_undelivered_orders_oblig_transferred_unpaid_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl488100_upward_adjust_pri_undeliv_order_oblig_unpaid_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl490100_delivered_orders_obligations_unpaid_fyb = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl490100_delivered_orders_obligations_unpaid_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl493100_delivered_orders_oblig_transferred_unpaid_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl498100_upward_adjust_pri_deliv_orders_oblig_unpaid_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl480200_undelivered_orders_oblig_prepaid_advanced_fyb = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl480200_undelivered_orders_oblig_prepaid_advanced_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl483200_undeliv_orders_oblig_transferred_prepaid_adv_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl488200_up_adjust_pri_undeliv_order_oblig_ppaid_adv_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl490200_delivered_orders_obligations_paid_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl490800_authority_outlayed_not_yet_disbursed_fyb = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl490800_authority_outlayed_not_yet_disbursed_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl498200_upward_adjust_pri_deliv_orders_oblig_paid_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    obligations_undelivered_orders_unpaid_total_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    obligations_delivered_orders_unpaid_total_fyb = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    obligations_delivered_orders_unpaid_total_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    gross_outlays_undelivered_orders_prepaid_total_fyb = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    gross_outlays_undelivered_orders_prepaid_total_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    gross_outlays_delivered_orders_paid_total_fyb = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    gross_outlay_amount_by_award_fyb = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    gross_outlay_amount_by_award_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    obligations_incurred_total_by_award_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl487100_down_adj_pri_unpaid_undel_orders_oblig_recov_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl497100_down_adj_pri_unpaid_deliv_orders_oblig_recov_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl487200_down_adj_pri_ppaid_undel_orders_oblig_refund_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    ussgl497200_down_adj_pri_paid_deliv_orders_oblig_refund_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    deobligations_recoveries_refunds_of_prior_year_by_award_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    obligations_undelivered_orders_unpaid_total_fyb = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    gross_outlays_delivered_orders_paid_total_cpe = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    drv_award_id_field_type = models.CharField(max_length=10, blank=True, null=True)
    drv_obligations_incurred_total_by_award = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    reporting_period_start = models.DateField(blank=True, null=True)
    reporting_period_end = models.DateField(blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    certified_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'financial_accounts_by_awards'


class FinancialAccountsByAwardsTransactionObligations(DataSourceTrackedModel):
    financial_accounts_by_awards_transaction_obligations_id = models.AutoField(primary_key=True)
    financial_accounts_by_awards = models.ForeignKey('FinancialAccountsByAwards', models.CASCADE)
    submission = models.ForeignKey(SubmissionAttributes, models.CASCADE)
    transaction_obligated_amount = models.DecimalField(max_digits=21, decimal_places=2, blank=True, null=True)
    reporting_period_start = models.DateField(blank=True, null=True)
    reporting_period_end = models.DateField(blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    certified_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'financial_accounts_by_awards_transaction_obligations'


class Award(DataSourceTrackedModel):

    AWARD_TYPES = (
        ('U', 'Unknown Type'),
        ('02', 'Block Grant'),
        ('03', 'Formula Grant'),
        ('04', 'Project Grant'),
        ('05', 'Cooperative Agreement'),
        ('06', 'Direct Payment for Specified Use'),
        ('07', 'Direct Loan'),
        ('08', 'Guaranteed/Insured Loan'),
        ('09', 'Insurance'),
        ('10', 'Direct Payment unrestricted'),
        ('11', 'Other'),
        ('A', 'BPA Call'),
        ('B', 'Purchase Order'),
        ('C', 'Delivery Order'),
        ('D', 'Definitive Contract')
    )

    type = models.CharField(max_length=5, choices=AWARD_TYPES, verbose_name="Award Type", default='U', null=True)
    type_description = models.CharField(max_length=50, verbose_name="Award Type Description", default="Unknown Type", null=True)
    piid = models.CharField(max_length=50, blank=True, null=True)
    parent_award = models.ForeignKey('awards.Award', related_name='child_award', null=True)
    fain = models.CharField(max_length=30, blank=True, null=True)
    uri = models.CharField(max_length=70, blank=True, null=True)
    total_obligation = models.DecimalField(max_digits=15, decimal_places=2, null=True, verbose_name="Total Obligated")
    total_outlay = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    awarding_agency = models.ForeignKey(Agency, related_name='+', null=True)
    funding_agency = models.ForeignKey(Agency, related_name='+', null=True)
    date_signed = models.DateField(null=True, verbose_name="Award Date")
    recipient = models.ForeignKey(LegalEntity, null=True)
    description = models.CharField(max_length=4000, null=True, verbose_name="Award Description")
    period_of_performance_start_date = models.DateField(null=True, verbose_name="Start Date")
    period_of_performance_current_end_date = models.DateField(null=True, verbose_name="End Date")
    place_of_performance = models.ForeignKey(Location, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    certified_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    latest_submission = models.ForeignKey(SubmissionAttributes, null=True)

    def __str__(self):
        return '%s piid: %s fain: %s uri: %s' % (self.get_type_display(), self.piid, self.fain, self.uri)

    def __get_latest_transaction(self):
        return self.__get_transaction_set().latest("action_date")

    # We should only have either procurements or financial assistance awards
    def __get_transaction_set(self):
        # Do we have procurements or financial assistance awards?
        transaction_set = self.procurement_set
        if transaction_set.count() == 0:
            transaction_set = self.financialassistanceaward_set
        return transaction_set

    def get_type_description(self):
        description = [item for item in Award.AWARD_TYPES if item[0] == self.type]
        if len(description) == 0:
            return "Unknown Type"
        else:
            return description[0][1]

    def save(self, *args, **kwargs):
        self.type_description = self.get_type_description()
        super(Award, self).save(*args, **kwargs)

    def update_from_mod(self, mod):
        transaction_set = self.__get_transaction_set()
        transaction_latest = transaction_set.latest("action_date")
        transaction_earliest = transaction_set.earliest("action_date")
        self.awarding_agency = transaction_latest.awarding_agency
        self.certified_date = transaction_latest.certified_date
        self.data_source = transaction_latest.data_source
        self.date_signed = transaction_earliest.action_date
        self.description = transaction_latest.award_description
        self.funding_agency = transaction_latest.funding_agency
        self.last_modified_date = transaction_latest.last_modified_date
        self.latest_submission = transaction_latest.submission
        self.period_of_performance_start_date = transaction_earliest.action_date
        self.period_of_performance_current_end_date = transaction_latest.action_date
        self.place_of_performance = transaction_latest.place_of_performance
        self.recipient = transaction_latest.recipient
        self.total_obligation = transaction_set.aggregate(total_obs=Sum(F('federal_action_obligation')))['total_obs']
        # what txn-level fields do we sum to get the award's total outlay?
        # self.total_outlay = ??
        if hasattr(transaction_latest, 'assistance_type'):
            # this is a financial assistance award, so use assistance_type field
            self.type = transaction_latest.assistance_type
        else:
            # this is a contract
            self.type = transaction_latest.contract_award_type
        self.save()

    latest_award_transaction = property(__get_latest_transaction)  # models.ForeignKey('AwardAction')

    @staticmethod
    def get_or_create_contract_award(awarding_agency, recipient, piid, parent_award_id=None):
        """
        Look for a contract award that matches the parameters, or create one if it doesn't exist.

        Input parameters:
            awarding_agency: agency object associated with the award transaction
            recipient: the recipient object associated with the award transaction
            piid: the award transaction's piid (procurement identifier)
            parent_award_id (optional): the award transaction's parent award id (this is
                relevant for sub-awards)

            The following combination of attributes makes up a unique contract award:
            - piid
            - parent_award_id (referred to as idv piid in legacy data)
            - awarding sub tier agency code
            - recipient entity id (e.g., DUNS, legal entity id)
        """
        q_kwargs = {}

        q_kwargs['piid'] = piid
        q_kwargs['awarding_agency__subtier_agency__subtier_code'] = awarding_agency.subtier_agency.subtier_code
        q_kwargs['recipient'] = recipient
        if parent_award_id:
            q_kwargs['parent_award__piid'] = parent_award_id
        else:
            q_kwargs['parent_award'] = None

        # Look for a matching award
        # Do we want to log something if the the query below turns up
        # more than one award record?
        contract_award = Award.objects.all().filter(Q(**q_kwargs)).first()
        if contract_award:
            return contract_award
        else:
            parent_award = None
            if parent_award_id:
                # If we have a parent award id, recursively get/create the award for it
                parent_award = Award.get_or_create_contract_award(**{
                    'piid': parent_award_id,
                    'awarding_agency': awarding_agency,
                    'recipient': recipient})
            # Award not found, so create one
            contract_award = Award(**{
                'piid': piid,
                'awarding_agency': awarding_agency,
                'recipient': recipient,
                'parent_award': parent_award
            })
            contract_award.save()
            return contract_award

    @staticmethod
    def get_or_create_financial_assistance_award(awarding_agency, recipient=None, fain=None, uri=None):
        """
        Look for a financial_assistance award that matches the parameters, or create one if it doesn't exist.

        Input parameters:
            awarding_agency: agency object associated with the award transaction
            recipient (optional): the recipient object associated with the award transaction
            aggregate_flag (optional): when true, indicates an aggregate award
            fain: the award transaction's fain (federal award identification number)
            uri: the transaction's uri

            The following combination of attributes makes up a unique financial assistance award
            - fain or uri (if both are specified, fain takes precedence)
            - uri
            - awarding sub tier agency code
            - recipient entity id (e.g., DUNS, legal entity id), applicable to non-aggregate awards only
        """
        q_kwargs = {}

        q_kwargs['awarding_agency__subtier_agency__subtier_code'] = awarding_agency.subtier_agency.subtier_code
        q_kwargs['recipient'] = recipient
        if fain:
            q_kwargs['fain'] = fain
        elif uri:
            q_kwargs['uri'] = uri
        else:
            raise ValueError('Financial assistance transaction must have either a fain or a uri')

        # Look for a matching award
        # Do we want to log something if the the query below turns up
        # more than one award record?
        financial_assistance_award = Award.objects.all().filter(Q(**q_kwargs)).first()
        if financial_assistance_award:
            return financial_assistance_award
        else:
            # Award not found, so create one
            financial_assistance_award = Award(**{
                'uri': uri,
                'fain': fain,
                'awarding_agency': awarding_agency,
                'recipient': recipient,
            })
            financial_assistance_award.save()
            return financial_assistance_award

    @staticmethod
    def get_or_create_financial_award(awarding_agency, piid=None, fain=None, uri=None, parent_award_id=None):
        """
        Look for an award record that "fuzzy" matches a more limited set
        of information. We need to do this, for example, when loading financial
        award records from the broker, since those records don't have
        awarding subtier agency and receipient information.
        """
        info = None

        q_kwargs = {'awarding_agency': awarding_agency}
        if piid is not None:
            q_kwargs['piid'] = piid
            if parent_award_id is not None:
                q_kwargs['parent_award__piid'] = parent_award_id
            else:
                q_kwargs['parent_award'] = None
        elif fain is not None:
                q_kwargs['fain'] = fain
        elif uri is not None:
                q_kwargs['uri'] = uri
        else:
            raise ValueError(
                'Unable to find or create financial award record with the provided information: piid={}, '
                'fain={}, uri={}, parent_id={}'.format(piid, fain, uri, parent_award_id))

        # Look for a corresponding award record. We sort by recipient to make
        # sure the more "complete" award records that match are at the top
        # of the list.
        # todo: update criteria for choosing between multiple "fuzzy" matching awards when we get more info
        financial_award = Award.objects.all().filter(Q(**q_kwargs)).order_by('recipient')
        if financial_award.count() == 1:
            # do we want to return info about this scenario
            financial_award = financial_award[0]
        elif financial_award.count() > 1:
            # there are multiple award records that match the current award info + agency
            # use the first one and return some info
            financial_award = financial_award[0]
            info = (
                'Found multiple potential award matches and chose award record {}.'
                'File C award data: piid={}, parent_award_id={},fain={}, uri={}, cgac={}.'.format(
                    financial_award.pk, piid, parent_award_id, fain, uri,
                    awarding_agency__toptier_agency.cgac_code
                ))
        else:
            # No potential award amounts found, so create one
            parent_award = None
            if parent_award_id:
                # If we have a parent award id, recursively get/create the award for it
                parent_award = Award.get_or_create_financial_award(**{
                    'awarding_agency': awarding_agency,
                    'piid': parent_award_id})
            financial_award = Award(**{
                'piid': piid,
                'awarding_agency': awarding_agency,
                'fain': fain,
                'uri': uri,
                'parent_award': parent_award
            })
            financial_award.save()
            return financial_award

        return financial_award, info

    class Meta:
        db_table = 'awards'


class AwardAction(DataSourceTrackedModel):
    award = models.ForeignKey(Award, models.CASCADE, related_name="actions")
    usaspending_unique_transaction_id = models.CharField(max_length=256, blank=True, null=True)
    submission = models.ForeignKey(SubmissionAttributes, models.CASCADE)
    action_date = models.DateField(max_length=10, verbose_name="Transaction Date")
    action_type = models.CharField(max_length=1, blank=True, null=True)
    federal_action_obligation = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    modification_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Modification Number")
    awarding_agency = models.ForeignKey(Agency, related_name='%(app_label)s_%(class)s_awarding_agency', null=True)
    funding_agency = models.ForeignKey(Agency, related_name='%(app_label)s_%(class)s_funding_agency', null=True)
    recipient = models.ForeignKey(LegalEntity, null=True)
    award_description = models.CharField(max_length=4000, null=True)
    place_of_performance = models.ForeignKey(Location, null=True)
    drv_award_transaction_usaspend = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    drv_current_total_award_value_amount_adjustment = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    drv_potential_total_award_value_amount_adjustment = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    certified_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    # Override the save method so that after saving we always call update_from_mod on our Award
    def save(self, *args, **kwargs):
        super(AwardAction, self).save(*args, **kwargs)
        self.award.update_from_mod(self)

    class Meta:
        abstract = True


class Procurement(AwardAction):
    procurement_id = models.AutoField(primary_key=True)
    award = models.ForeignKey(Award, models.CASCADE)
    submission = models.ForeignKey(SubmissionAttributes, models.CASCADE)
    piid = models.CharField(max_length=50, blank=True)
    parent_award_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="Parent Award ID")
    cost_or_pricing_data = models.CharField(max_length=1, blank=True, null=True)
    type_of_contract_pricing = models.CharField(max_length=2, blank=True, null=True, verbose_name="Type of Contract Pricing")
    contract_award_type = models.CharField(max_length=1, blank=True, null=True, verbose_name="Contract Award Type")
    naics = models.CharField(max_length=6, blank=True, null=True, verbose_name="NAICS")
    naics_description = models.CharField(max_length=150, blank=True, null=True, verbose_name="NAICS Description")
    period_of_performance_potential_end_date = models.CharField(max_length=8, blank=True, null=True, verbose_name="Period of Performance Potential End Date")
    ordering_period_end_date = models.CharField(max_length=8, blank=True, null=True)
    current_total_value_award = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    potential_total_value_of_award = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, verbose_name="Potential Total Value of Award")
    referenced_idv_agency_identifier = models.CharField(max_length=4, blank=True, null=True)
    idv_type = models.CharField(max_length=1, blank=True, null=True, verbose_name="IDV Type")
    multiple_or_single_award_idv = models.CharField(max_length=1, blank=True, null=True)
    type_of_idc = models.CharField(max_length=1, blank=True, null=True, verbose_name="Type of IDC")
    a76_fair_act_action = models.CharField(max_length=1, blank=True, null=True, verbose_name="A-76 FAIR Act Action")
    dod_claimant_program_code = models.CharField(max_length=3, blank=True, null=True)
    clinger_cohen_act_planning = models.CharField(max_length=1, blank=True, null=True)
    commercial_item_acquisition_procedures = models.CharField(max_length=1, blank=True, null=True)
    commercial_item_test_program = models.CharField(max_length=1, blank=True, null=True)
    consolidated_contract = models.CharField(max_length=1, blank=True, null=True)
    contingency_humanitarian_or_peacekeeping_operation = models.CharField(max_length=1, blank=True, null=True)
    contract_bundling = models.CharField(max_length=1, blank=True, null=True)
    contract_financing = models.CharField(max_length=1, blank=True, null=True)
    contracting_officers_determination_of_business_size = models.CharField(max_length=1, blank=True, null=True)
    cost_accounting_standards = models.CharField(max_length=1, blank=True, null=True)
    country_of_product_or_service_origin = models.CharField(max_length=3, blank=True, null=True)
    davis_bacon_act = models.CharField(max_length=1, blank=True, null=True)
    evaluated_preference = models.CharField(max_length=6, blank=True, null=True)
    extent_competed = models.CharField(max_length=3, blank=True, null=True)
    fed_biz_opps = models.CharField(max_length=1, blank=True, null=True)
    foreign_funding = models.CharField(max_length=1, blank=True, null=True)
    gfe_gfp = models.CharField(max_length=1, blank=True, null=True)
    information_technology_commercial_item_category = models.CharField(max_length=1, blank=True, null=True)
    interagency_contracting_authority = models.CharField(max_length=1, blank=True, null=True)
    local_area_set_aside = models.CharField(max_length=1, blank=True, null=True)
    major_program = models.CharField(max_length=100, blank=True, null=True)
    purchase_card_as_payment_method = models.CharField(max_length=1, blank=True, null=True)
    multi_year_contract = models.CharField(max_length=1, blank=True, null=True)
    national_interest_action = models.CharField(max_length=4, blank=True, null=True)
    number_of_actions = models.CharField(max_length=6, blank=True, null=True)
    number_of_offers_received = models.CharField(max_length=3, blank=True, null=True)
    other_statutory_authority = models.CharField(max_length=1000, blank=True, null=True)
    performance_based_service_acquisition = models.CharField(max_length=1, blank=True, null=True)
    place_of_manufacture = models.CharField(max_length=1, blank=True, null=True)
    price_evaluation_adjustment_preference_percent_difference = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    product_or_service_code = models.CharField(max_length=4, blank=True, null=True)
    program_acronym = models.CharField(max_length=25, blank=True, null=True)
    other_than_full_and_open_competition = models.CharField(max_length=3, blank=True, null=True)
    recovered_materials_sustainability = models.CharField(max_length=1, blank=True, null=True)
    research = models.CharField(max_length=3, blank=True, null=True)
    sea_transportation = models.CharField(max_length=1, blank=True, null=True)
    service_contract_act = models.CharField(max_length=1, blank=True, null=True)
    small_business_competitiveness_demonstration_program = models.CharField(max_length=1, blank=True, null=True)
    solicitation_identifier = models.CharField(max_length=25, blank=True, null=True, verbose_name="Solicitation ID")
    solicitation_procedures = models.CharField(max_length=5, blank=True, null=True)
    fair_opportunity_limited_sources = models.CharField(max_length=50, blank=True, null=True)
    subcontracting_plan = models.CharField(max_length=1, blank=True, null=True)
    program_system_or_equipment_code = models.CharField(max_length=4, blank=True, null=True)
    type_set_aside = models.CharField(max_length=10, blank=True, null=True, verbose_name="Type Set Aside")
    epa_designated_product = models.CharField(max_length=1, blank=True, null=True)
    walsh_healey_act = models.CharField(max_length=1, blank=True, null=True)
    transaction_number = models.CharField(max_length=6, blank=True, null=True)
    referenced_idv_modification_number = models.CharField(max_length=25, blank=True, null=True)
    rec_flag = models.CharField(max_length=1, blank=True, null=True)
    drv_parent_award_awarding_agency_code = models.CharField(max_length=4, blank=True, null=True)
    drv_current_aggregated_total_value_of_award = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    drv_current_total_value_of_award = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    drv_potential_award_idv_amount_total_estimate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    drv_potential_aggregated_award_idv_amount_total_estimate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    drv_potential_aggregated_total_value_of_award = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    drv_potential_total_value_of_award = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    certified_date = models.DateField(blank=True, null=True)
    reporting_period_start = models.DateField(blank=True, null=True)
    reporting_period_end = models.DateField(blank=True, null=True)


class FinancialAssistanceAward(AwardAction):
    financial_assistance_award_id = models.AutoField(primary_key=True)
    award = models.ForeignKey(Award, models.CASCADE)
    submission = models.ForeignKey(SubmissionAttributes, models.CASCADE)
    fain = models.CharField(max_length=30, blank=True, null=True)
    uri = models.CharField(max_length=70, blank=True, null=True)
    cfda_number = models.CharField(max_length=7, blank=True, null=True, verbose_name="CFDA Number")
    cfda_title = models.CharField(max_length=250, blank=True, null=True, verbose_name="CFDA Title")
    business_funds_indicator = models.CharField(max_length=3)
    non_federal_funding_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    total_funding_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    face_value_loan_guarantee = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    original_loan_subsidy_cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    assistance_type = models.CharField(max_length=2, verbose_name="Assistance Type")
    record_type = models.IntegerField()
    correction_late_delete_indicator = models.CharField(max_length=1, blank=True, null=True)
    fiscal_year_and_quarter_correction = models.CharField(max_length=5, blank=True, null=True)
    sai_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="SAI Number")
    drv_federal_funding_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    drv_award_finance_assistance_type_label = models.CharField(max_length=50, blank=True, null=True)
    reporting_period_start = models.DateField(blank=True, null=True)
    reporting_period_end = models.DateField(blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    submitted_type = models.CharField(max_length=1, blank=True, null=True, verbose_name="Submitted Type")
    certified_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'financial_assistance_award'


class SubAward(DataSourceTrackedModel):
    sub_award_id = models.AutoField(primary_key=True, verbose_name="Sub-Award ID")
    award = models.ForeignKey(Award, models.CASCADE)
    legal_entity = models.ForeignKey(LegalEntity, models.CASCADE)
    sub_recipient_unique_id = models.CharField(max_length=9, blank=True, null=True)
    sub_recipient_ultimate_parent_unique_id = models.CharField(max_length=9, blank=True, null=True)
    sub_recipient_ultimate_parent_name = models.CharField(max_length=120, blank=True, null=True)
    subawardee_business_type = models.CharField(max_length=255, blank=True, null=True)
    sub_recipient_name = models.CharField(max_length=120, blank=True, null=True)
    subcontract_award_amount = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    cfda_number_and_title = models.CharField(max_length=255, blank=True, null=True)
    prime_award_report_id = models.CharField(max_length=40, blank=True, null=True)
    award_report_month = models.CharField(max_length=25, blank=True, null=True)
    award_report_year = models.CharField(max_length=4, blank=True, null=True)
    rec_model_question1 = models.CharField(max_length=1, blank=True, null=True)
    rec_model_question2 = models.CharField(max_length=1, blank=True, null=True)
    subaward_number = models.CharField(max_length=32, blank=True, null=True)
    reporting_period_start = models.DateField(blank=True, null=True)
    reporting_period_end = models.DateField(blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    certified_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'sub_award'
