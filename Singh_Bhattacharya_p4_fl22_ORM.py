from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
import logging


engine = create_engine('sqlite:///sales.db', echo = True)


Base = declarative_base()
metadata = MetaData(engine)

class Employee(Base):
   __tablename__ = 'Employee'

   employeeid = Column(Integer, primary_key=True)
   fname = Column(String)
   mname = Column(String)
   lname = Column(String)
   address = Column(String)
   startdate = Column(String)
   enddate = Column(String)
   pay = Column(Integer)


class DateDimension(Base):
   __tablename__ = 'DateDimension'

   dateid = Column(Integer, primary_key=True)
   date = Column(String)
   year = Column(String)
   quarter = Column(String)
   monthnum = Column(String)
   monthname = Column(String)
   dayofmonth = Column(String)
   dayofweek = Column(String)
   dayname = Column(String)

class Address(Base):
   __tablename__ = 'Address'

   addressid = Column(Integer, primary_key=True)
   zipcode = Column(Integer)
   street = Column(String)
   apartment = Column(String)
   country = Column(String)
   state = Column(String)
   city = Column(String)



class Policy(Base):
   __tablename__ = 'Policy'

   policyid = Column(Integer, primary_key=True)
   policyexpirydate = Column(String)
   policyeffectivedate = Column(String)
   policynumber = Column(String)
   amount = Column(Integer)
   copay = Column(Integer)


class HealthAttributes(Base):
   __tablename__ = 'HealthAttributes'

   attributesid = Column(Integer, primary_key=True)
   paintlocation = Column(String)
   paintexertion = Column(String)
   relievedafterrest = Column(String)
   chestpaintype = Column(String)
   smokingstatus = Column(String)
   diagnosis = Column(String)
   classDisease = Column(String)
   steroid = Column(String)
   antivirals = Column(String)
   fatigue = Column(String)

class Customers(Base):
   __tablename__ = 'Customers'
   
   customerid = Column(Integer, primary_key = True)
   policyid = Column(Integer, ForeignKey(Policy.policyid))
   addressid = Column(Integer, ForeignKey(Address.addressid))
   Fname = Column(String)
   Mname = Column(String)
   Lname = Column(String)
   Suffix = Column(String)
   Prefix = Column(String)
   Email = Column(String)
   Gender = Column(String)
   Phone = Column(String)
   HealthAttributesID = Column(String, ForeignKey(HealthAttributes.attributesid))
   SSN = Column(Integer)
   Age = Column(Integer)
   Sex = Column(String)

class Plan(Base):
   __tablename__ = 'Plan'
   
   planid = Column(Integer, primary_key = True)
   name = Column(String)
   description = Column(String)
   AnnualizedPremium = Column(Integer)
   Benefit = Column(String)
   IssueDateId = Column(String, ForeignKey(DateDimension.dateid))
   policyID = Column(Integer, ForeignKey(Policy.policyid))

class RevenueSnapshot(Base):
   __tablename__ = 'RevenueSnapshot'

   customerid = Column(Integer, ForeignKey(Customers.customerid))
   monthendsnaposhotid = Column(Integer, primary_key=True)
   Agentid = Column(Integer, ForeignKey(Employee.employeeid))
   planid = Column(Integer, ForeignKey(Plan.planid))
   policystatusid = Column(Integer)
   policynumberid = Column(Integer, ForeignKey(Policy.policyid))
   aggregateamount = Column(Integer)
   monthlyamount = Column(Integer)

class ProfitLossSnapshot(Base):
   __tablename__ = 'ProfitLossSnapshot'

   customerid = Column(Integer, ForeignKey(Customers.customerid))
   plid = Column(Integer, primary_key=True)
   monthendsnaposhotid = Column(Integer, ForeignKey(RevenueSnapshot.monthendsnaposhotid))
   Agentid = Column(Integer, ForeignKey(Employee.employeeid))
   planid = Column(Integer, ForeignKey(Plan.planid))
   policystatusid = Column(Integer)
   policynumberid = Column(Integer, ForeignKey(Policy.policyid))
   aggregateamount = Column(Integer)
   monthlyamount = Column(Integer)
   claimpaidamount = Column(Integer)
   claimcollectedamount = Column(Integer)

class Invoice(Base):
   __tablename__ = 'Invoice'

   invoiceid = Column(Integer, primary_key=True)
   customerid = Column(Integer, ForeignKey(Customers.customerid))
   addressid = Column(Integer, ForeignKey(Address.addressid))
   phonenumber = Column(Integer)
   planid = Column(Integer)
   amount = Column(Integer)

class PolicyTransactions(Base):
   __tablename__ = 'PolicyTransactions'

   transactionid = Column(Integer, primary_key=True)
   accountid = Column(Integer)
   invoiceid = Column(Integer, ForeignKey(Invoice.invoiceid))
   policynumberid = Column(Integer, ForeignKey(Policy.policyid))
   policytransid = Column(String)
   ptstartbydate = Column(String)
   ptbuydate = Column(Integer)
   customerid = Column(Integer, ForeignKey(Customers.customerid))
   agentid = Column(Integer, ForeignKey(Employee.employeeid))
   planid = Column(Integer, ForeignKey(Plan.planid))


class ClaimTransaction(Base):
   __tablename__ = 'ClaimTransaction'

   claimtransactionid = Column(Integer, primary_key=True)
   agentid = Column(Integer, ForeignKey(Employee.employeeid))
   customerid = Column(Integer, ForeignKey(Customers.customerid))
   policynumberid = Column(Integer, ForeignKey(Policy.policyid))
   claimantid = Column(Integer, ForeignKey(Employee.employeeid))
   claimeffectivedate = Column(String)
   claimsettlementdate = Column(String)
   claimamount = Column(Integer)
   claimimage = Column(Integer)
   claimemployee = Column(Integer, ForeignKey(Employee.employeeid))

class ClaimProgression(Base):
   __tablename__ = 'ClaimProgression'

   progressionid = Column(Integer, primary_key=True)
   closedate = Column(String, ForeignKey(DateDimension.dateid))
   opendate = Column(String, ForeignKey(DateDimension.dateid))
   mostrecentpayment = Column(Integer)
   estimatedate = Column(Integer, ForeignKey(DateDimension.dateid))
   employeeid = Column(Integer, ForeignKey(Employee.employeeid))
   customerid = Column(Integer,  ForeignKey(Customers.customerid))
   claimid = Column(Integer)
   policynumberid = Column(Integer, ForeignKey(Policy.policyid))
   claimemployee = Column(Integer,  ForeignKey(Customers.customerid))

    
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

