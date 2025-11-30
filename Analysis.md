
# PageSpeed Insights Analysis

A full performance evaluation was conducted using Google PageSpeed Insights on both mobile and desktop. The results show that the application is highly optimized across all metrics and platforms.


## Mobile Results

**Scores**

* **Performance:** 98
* **Accessibility:** 100
* **Best Practices:** 100
* **SEO:** 91

**Core Metrics**

* **First Contentful Paint (FCP):** 1.8s
* **Largest Contentful Paint (LCP):** 1.9s
* **Total Blocking Time (TBT):** 0ms
* **Cumulative Layout Shift (CLS):** 0
* **Speed Index:** 1.8s
* Tested on *Moto G Power emulation* with *slow 4G throttling*.

**Insights / Opportunities**

* Reduce render-blocking resources (est. 150ms savings).
* Improve image delivery (est. 1,355 KiB savings).
* Optimize viewport for mobile devices.
* Reduce unused CSS (est. 31 KiB savings).


## Desktop Results

**Scores**

* **Performance:** 100
* **Accessibility:** 100
* **Best Practices:** 100
* **SEO:** 91

**Core Metrics**

* **First Contentful Paint (FCP):** 0.5s
* **Largest Contentful Paint (LCP):** 0.5s
* **Total Blocking Time (TBT):** 0ms
* **Cumulative Layout Shift (CLS):** 0
* **Speed Index:** 0.5s
* Tested using *desktop emulation* with custom throttling.

**Insights / Opportunities**

* Reduce render-blocking resources (est. 240ms savings).
* Improve image delivery (same 1,355 KiB savings).
* Reduce unused CSS (est. 30 KiB savings).


## Summary

Both the mobile and desktop Lighthouse results show that the site performs exceptionally well. There is no blocking time and no layout shift on either platform, and both accessibility and best practice scores are perfect. The only notable limitation on SEO is the absence of a meta description tag. Aside from that, the remaining suggestions such as; optimizing images, removing unused CSS, and minimizing any blocking resources, are minor refinements rather than major performance issues.

