#include <cmath>
#include <iostream>
using namespace std;

double couponBondPrice(double t,double maturity,double principle,double coupon,double interestRate,int couponsPerYear)
{
  // store the value of the bond
  double bondValue=0.;
  // add in coupons
  int startCoupon=floor(t*couponsPerYear) + 1;
  int totalNumberCoupons=maturity*couponsPerYear;
  for(int i=startCoupon;i<=totalNumberCoupons;i++)
  {
    double ti=double(i)/double(couponsPerYear);
    cout << ti;
    bondValue = bondValue + coupon*exp(-interestRate*(ti-t));
  }
  // finally add principle
  if(t<=maturity)
    bondValue = bondValue + principle*exp(-interestRate*(maturity-t));
  return bondValue;
}

int main()
{
  // output bond price  
  cout << " The value of the bond is " << couponBondPrice(0.1, 4., 100.,5.,0.05,1) <<endl;
  return 0;
}